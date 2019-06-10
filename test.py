from justlog import justlog, settings
from justlog.classes import Severity, Output, Format


logger_stdout = justlog.Logger(settings.Settings())
logger_json = justlog.Logger(settings.Settings())


logger_json.settings.current_log_level = Severity.ERR
logger_json.settings.log_output = Output.FILE
logger_json.settings.log_format = Format.JSON
logger_json.settings.log_file = "/tmp/sample.json"
logger_json.settings.update_field("application", "sample")
logger_json.settings.update_field("level", "$CURRENT_LOG_LEVEL")
logger_json.settings.update_field("timestamp", "$TIMESTAMP")

logger_stdout.settings.colorized_logs = True
logger_stdout.settings.log_output = Output.TCP
logger_stdout.settings.update_field("application", "sample")
logger_stdout.settings.update_field("timestamp", "$TIMESTAMP")
logger_stdout.settings.update_field("level", "$CURRENT_LOG_LEVEL")
logger_stdout.settings.string_format = "[ $timestamp ] :: Level: $CURRENT_LOG_LEVEL, application: $application"

logger_stdout.info("Information")
logger_stdout.error("Error")
logger_stdout.warning("Warning")
logger_stdout.debug("Debug")
logger_json.log("Some text to send as json")
