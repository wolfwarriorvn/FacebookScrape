from colorama import Fore, Back, Style
from enum import Enum

class LogLevel(Enum):
    NONE = 0
    DEBUG = 1
    ERROR = 2

def log(log_level: LogLevel, data):
    if log_level is LogLevel.DEBUG:
        print(Fore.GREEN)
        print(data)
    elif log_level is LogLevel.ERROR:
        print(Fore.RED)
        print(data)
    print(Style.RESET_ALL)  