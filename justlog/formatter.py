import json
import datetime
from .settings import Settings


def json_formatter(settings: Settings):
    settings.update_field("message", settings.message)
    settings.message = json.dumps(settings.fields)
    return builtins_formatter(settings)

def text_formatter(settings: Settings):
    buffer = settings.string_format
    settings.update_field("message", settings.message)
    for field in settings.fields:
        buffer = buffer.replace(f"${field}", settings.fields[field])
    settings.message = buffer
    return builtins_formatter(settings)

def builtins_formatter(settings: Settings):
    """Format values that need to be evaluated on every call."""
    buffer = settings.message.replace("$CURRENT_LOG_LEVEL", settings.log_level_name())
    buffer = buffer.replace("$TIMESTAMP", f"{datetime.datetime.now().strftime(settings.timestamp_format)}")
    settings.message = buffer
    return settings
