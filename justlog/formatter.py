import json
import datetime
from .settings import Settings

# Format output to json
def json_formatter(settings: Settings):
    settings.update_field("message", settings.message)
    settings.message = json.dumps(settings.fields)
    return builtins_formatter(settings)


# Format output to text
def text_formatter(settings: Settings):
    buffer = settings.string_format
    settings.update_field("message", settings.message)
    for field in settings.fields:
        buffer = buffer.replace(f"${field}", settings.fields[field])
    settings.message = buffer
    return builtins_formatter(settings)


# Format values changed when called (Ex: timestamp)
def builtins_formatter(settings: Settings):
    buffer = settings.message.replace("$CURRENT_LOG_LEVEL", settings.log_level_name())
    buffer = buffer.replace(
        "$TIMESTAMP", f"{datetime.datetime.now().strftime(settings.timestamp_format)}"
    )
    settings.message = buffer
    return settings
