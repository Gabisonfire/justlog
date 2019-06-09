from enum import IntEnum, Enum

class Severity(IntEnum):
    DBG = 1
    INF = 2
    WRN = 3
    ERR = 4

class Format(Enum):
    JSON = 0
    TEXT = 1

class Output(Enum):
    STDOUT = 0
    FILE = 1
    SYSLOG = 2
