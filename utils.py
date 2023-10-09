from colorama import Fore, Back, Style
from enum import Enum
from random import randrange
from PIL import Image
import hashlib
import pyexiv2
import uuid

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

def get_md5_image_pixel(img_file):
    md5hash = hashlib.md5(Image.open(img_file).tobytes())
    return md5hash.hexdigest()

def get_md5_file(img_file):
    with open(img_file, 'rb+') as img_file:
        md5hash = hashlib.md5(img_file.read())
        return md5hash.hexdigest()
    
def random_metadata_image(img_file):
    try:
        with pyexiv2.Image(img_file) as img:
            img.modify_comment('{}'.format(uuid.uuid4()))
            img.modify_xmp({'Xmp.dc.subject': uuid.uuid4()})
    except Exception as e:
        pass
def random_md5_image(img_file):
    #random pixel data at x,y: 0,0
    img = Image.open(img_file)
    value = (randrange(0,255), randrange(0,255), randrange(0,255))
    img.putpixel((0,0), value)
    img.save(img_file)
    random_metadata_image(img_file)