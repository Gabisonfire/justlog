from enum import IntEnum, Enum


class Severity(IntEnum):
    """
    Defines a degree of logging.
    """

    DBG = 1
    INF = 2
    WRN = 3
    ERR = 4


class Format(Enum):
    """
    Defines the output format for the logs.
    """

    JSON = 0
    TEXT = 1


class Output(Enum):
    """
    Defines the output(s) for the logs.
    """

    STDOUT = 0
    STDERR = 1
    FILE = 2
    SYSLOG = 3
    HTTP = 4
    TCP = 5
