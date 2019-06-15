## justlog ##

[Documentation](https://justlog.readthedocs.io/en/latest/)

justlog is a simple library for Python 3. It is designed to provide a quick and easy way to generate clean logs with minimal coding.

### Features ###

- Output to to stdout, stderr, tcp, http, file or syslog
- Output in standard text or json
- Easily add fields
- Builtin variables for timestamps and log levels.
- Colorful output

### Quickstart ###

```python
from justlog import justlog, settings
from justlog.classes import Severity, Output, Format

logger_stdout = justlog.Logger(settings.Settings())
logger_stdout.settings.colorized_logs = True
logger_stdout.settings.log_output = Output.STDOUT
logger_stdout.settings.update_field("application", "sample")
logger_stdout.settings.update_field("timestamp", "$TIMESTAMP")
logger_stdout.settings.update_field("level", "$CURRENT_LOG_LEVEL")
logger_stdout.settings.string_format = "[ $timestamp ] :: Level: $CURRENT_LOG_LEVEL, application: $application"

logger_stdout.info("Information")
logger_stdout.error("Error")
logger_stdout.warning("Warning")
logger_stdout.debug("Debug")
```

### Installation ###

```python
pip install justlog
```

### License ###

- MIT
