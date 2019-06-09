# justlog

A simple library for logging with Python3

## Basics

For a quick example, refer to the test.py on the [github repository](https://github.com/Gabisonfire/justlog/blob/master/test.py)

With justlog, everything is handled within a single class: `Logger`

Spawn an instance of this class to start logging quickly.
```python
from justlog import justlog, settings
logger = justlog.Logger(settings.Settings())
```
Instances must be initialized with a `Settings` instance that can be customized before or after instantiation.

## Syntax ##
### Logger ###
- `log(message)`
    - message: The message to log
    - Will use the current log level set within the `Settings` class: `logger.settings.current_log_level`
- `debug(message)`
    - message: The message to log
    - Sets the `current_log_level` to `Severity.DBG` and calls the `log()` function 
- `info(message)`
    - message: The message to log
    - Sets the `current_log_level` to `Severity.INF` and calls the `log()` function 
- `warning(message)`
    - message: The message to log
    - Sets the `current_log_level` to `Severity.WRN` and calls the `log()` function 
- `error(message)`
    - message: The message to log
    - Sets the `current_log_level` to `Severity.ERR` and calls the `log()` function 

### Settings ###
- `appname: str`
    - Used as a default for various other settings like the log path
- `current_log_level: Severity`
    - Sets the current log level. Influences colors and fields.
    - Log levels: `DBG` `INF` `WRN` `ERR`
- `colorized_logs: Bool`
    - Enables or disables the log coloration for different `Severity`
- `log_format: Format`
    - Sets the log format type
    - `TEXT` `JSON`
- `log_output: Output`
    - Defines where the logs are output
    - `STDOUT` `FILE` `SYSLOG`
- `string_format: str`
    - Defines the template and fields for logs output in the `TEXT` format
- `timestamp_format`
    - Sets the `$TIMESTAMP` variable format using [stfrtime codes](http://strftime.org/)
- `update_field(key: str, value: str)`
    - Adds or updates a field that will be output to the logs. Fields can be reffered using the `$` symbol within the `string_format`
- `delete_field(key: str)`
    - Removes a field

### Builtin Variables ###
- `$TIMESTAMP`
    - Will print the current time in the format defined by the `timestamp_format` setting using [stfrtime codes](http://strftime.org/)
- `$CURRENT_LOG_LEVEL`
    - Will print the current log level based on the  `current_log_level` setting at the moment of the call.
