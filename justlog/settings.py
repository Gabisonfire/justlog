from .classes import Severity, Output, Format

class Settings():
    """Class to set logging parameters"""
    def __init__(self):
        self.message = ""
        self.app_name = "justlog"
        self.current_log_level = Severity.INF
        self.colorized_logs = False
        self.log_format = Format.TEXT
        self.log_output = []
        self.log_file = f"/tmp/{self.app_name}"
        self.fields = {}
        self.string_format = ""
        self.timestamp_format = "%Y-%m-%d %X.%f"
        self.tcp_output_host = ""
        self.tcp_output_port = 5000
        self.http_url = ""
        self.http_headers = {}
        self.http_print_response = False
    def update_field(self, key, value):
        self.fields.update({key:value})
    def delete_field(self, key):
        del self.fields[key]
    def log_level_name(self):
        return self.current_log_level.name
