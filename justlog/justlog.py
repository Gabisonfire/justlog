import syslog
import sys
import socket
from colorama import init, Fore
from .settings import Settings
from .classes import Severity, Output, Format
from .formatter import json_formatter, text_formatter

init()

class Logger(Settings):
    def __init__(self, settings):
        self.settings = settings

    def log(self, message):
        self.settings.message = message
        if not isinstance(self.settings.log_format, Format):
            raise TypeError(f"Unsupported or unrecognized format: {type(self.settings.log_format)}")
        if not isinstance(self.settings.log_output, Output):
            raise TypeError(f"Unsupported or unrecognized output: {type(self.settings.log_output)}")
        if not isinstance(self.settings.current_log_level, Severity):
            raise TypeError(f"Unsupported or unrecognized severity: {type(self.settings.current_log_level)}")
        if self.settings.log_format == Format.JSON:
            self.settings = json_formatter(self.settings)
        if self.settings.log_format == Format.TEXT:
            self.settings = text_formatter(self.settings)
        if self.settings.log_output == Output.STDOUT:
            log_to_stdout(self.settings)
        if self.settings.log_output == Output.STDERR:
            log_to_stderr(self.settings)
        if self.settings.log_output == Output.FILE:
            log_to_file(self.settings.message, self.settings.log_file)
        if self.settings.log_output == Output.SYSLOG:
            log_to_sys(self.settings.message, self.settings.current_log_level)
        if self.settings.log_output == Output.TCP:
            log_to_tcp(self.settings.message, self.settings)
        self.settings.message = ""
    def debug(self, message):
        self.settings.current_log_level = Severity.DBG
        self.log(message)
    def info(self, message):
        self.settings.current_log_level = Severity.INF
        self.log(message)
    def warning(self, message):
        self.settings.current_log_level = Severity.WRN
        self.log(message)
    def error(self, message):
        self.settings.current_log_level = Severity.ERR
        self.log(message)

def log_to_stdout(settings: Settings):
    reset = Fore.RESET
    color = Fore.WHITE
    if settings.colorized_logs:
        if settings.current_log_level == Severity.WRN:
            color = Fore.YELLOW
        if settings.current_log_level == Severity.ERR:
            color = Fore.RED
    print(f"{color}{settings.message}{reset}")

def log_to_stderr(settings: Settings):
    reset = Fore.RESET
    color = Fore.WHITE
    if settings.colorized_logs:
        if settings.current_log_level == Severity.WRN:
            color = Fore.YELLOW
        if settings.current_log_level == Severity.ERR:
            color = Fore.RED
    print(f"{color}{settings.message}{reset}", file=sys.stderr)

def log_to_file(message, log_file):
    f = open(log_file, "a+")
    f.write(message + "\n")
    f.close()

def log_to_sys(message, severity):
    if severity == Severity.DBG:
        syslog.syslog(syslog.LOG_DEBUG, message)
    if severity == Severity.INF:
        syslog.syslog(syslog.LOG_INFO, message)
    if severity == Severity.WRN:
        syslog.syslog(syslog.LOG_WARNING, message)
    if severity == Severity.ERR:
        syslog.syslog(syslog.LOG_ERR, message)

def log_to_tcp(message, settings):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((settings.tcp_output_host, settings.tcp_output_port))
        sock.sendall(bytes(message + "\n", "utf-8"))
        sock.close()
