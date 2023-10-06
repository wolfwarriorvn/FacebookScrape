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

def convert_str_to_number(x):
    total_stars = 0
    num_map = {'K':1000, 'M':1000000, 'B':1000000000}
    if x.isdigit():
        total_stars = int(x)
    else:
        if len(x) > 1:
            total_stars = float(x[:-1]) * num_map.get(x[-1].upper(), 1)
    return str(int(total_stars))

# Công khai · 13K thành viên · 4 bài viết/ngày
def extract_raw_group_info(info_text):
    info = info_text.split('·', maxsplit=2)
    category, members_text, details = ['','','']
    if len(info) == 1:
        category = info
    elif len(info) == 2:
        category, members_text = info
    elif len(info) == 3:
        category, members_text, details = info
    return category, members_text, details