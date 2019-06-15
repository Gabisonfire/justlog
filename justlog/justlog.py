import syslog
import sys
import socket
import requests
from colorama import init, Fore
from .settings import Settings
from .classes import Severity, Output, Format
from .formatter import json_formatter, text_formatter

init()


class Logger(Settings):
    """Holds all settings and main methods for logging."""

    def __init__(self, settings):
        self.settings = settings

    def log(self, message):
        """Log a message.

        Args:
            message: The message to log.
        """
        self.settings.message = message
        if not isinstance(self.settings.log_format, Format):
            raise TypeError(
                f"Unsupported or unrecognized format: {type(self.settings.log_format)}"
            )
        for output in self.settings.log_output:
            if not isinstance(output, Output):
                raise TypeError(f"Unsupported or unrecognized output: {type(output)}")
        if not isinstance(self.settings.current_log_level, Severity):
            raise TypeError(
                f"Unsupported or unrecognized severity: {type(self.settings.current_log_level)}"
            )
        if self.settings.log_format == Format.JSON:
            self.settings = json_formatter(self.settings)
        if self.settings.log_format == Format.TEXT:
            self.settings = text_formatter(self.settings)
        if Output.STDOUT in self.settings.log_output:
            log_to_stdout(self.settings)
        if Output.STDERR in self.settings.log_output:
            log_to_stderr(self.settings)
        if Output.FILE in self.settings.log_output:
            log_to_file(self.settings.message, self.settings.log_file)
        if Output.SYSLOG in self.settings.log_output:
            log_to_sys(self.settings.message, self.settings.current_log_level)
        if Output.TCP in self.settings.log_output:
            log_to_tcp(self.settings.message, self.settings)
        if Output.HTTP in self.settings.log_output:
            log_to_http(self.settings.message, self.settings)
        self.settings.message = ""

    def debug(self, message):
        """Logs a message with the 'Debug' level.

        Args:
            message: The message to log.
        """
        self.settings.current_log_level = Severity.DBG
        self.log(message)

    def info(self, message):
        """Logs a message with the 'Info' level.

        Args:
            message: The message to log.
        """
        self.settings.current_log_level = Severity.INF
        self.log(message)

    def warning(self, message):
        """Logs a message with the 'Warning' level.

        Args:
            message: The message to log.
        """
        self.settings.current_log_level = Severity.WRN
        self.log(message)

    def error(self, message):
        """Logs a message with the 'Error' level.

        Args:
            message: The message to log.
        """
        self.settings.current_log_level = Severity.ERR
        self.log(message)


# Log to stout
def log_to_stdout(settings: Settings):
    reset = Fore.RESET
    color = Fore.WHITE
    if settings.colorized_logs:
        if settings.current_log_level == Severity.WRN:
            color = Fore.YELLOW
        if settings.current_log_level == Severity.ERR:
            color = Fore.RED
    print(f"{color}{settings.message}{reset}")


# Log to stderr
def log_to_stderr(settings: Settings):
    reset = Fore.RESET
    color = Fore.WHITE
    if settings.colorized_logs:
        if settings.current_log_level == Severity.WRN:
            color = Fore.YELLOW
        if settings.current_log_level == Severity.ERR:
            color = Fore.RED
    print(f"{color}{settings.message}{reset}", file=sys.stderr)


# Append log to file, create if non existent
def log_to_file(message, log_file):
    _file = open(log_file, "a+")
    _file.write(message + "\n")
    _file.close()


# Send logs to syslog (journal)
def log_to_sys(message, severity):
    if severity == Severity.DBG:
        syslog.syslog(syslog.LOG_DEBUG, message)
    if severity == Severity.INF:
        syslog.syslog(syslog.LOG_INFO, message)
    if severity == Severity.WRN:
        syslog.syslog(syslog.LOG_WARNING, message)
    if severity == Severity.ERR:
        syslog.syslog(syslog.LOG_ERR, message)


# Log to tcp output using socket
def log_to_tcp(message, settings):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((settings.tcp_output_host, settings.tcp_output_port))
        sock.sendall(bytes(message + "\n", "utf-8"))
        sock.close()


# Lof to http using POST
def log_to_http(message, settings):
    req = requests.post(settings.http_url, message, headers=settings.http_headers)
    if settings.http_print_response:
        print(req.content)
