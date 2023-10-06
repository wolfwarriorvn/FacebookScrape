import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from facebook_scraper import FacebookScraper
from time import sleep
import random
import glob

_uid = "100095589726697"
_pw = "ak47@1992"
_proxy = "None"
_pageid = "100053555150984"

fb_scraper = FacebookScraper(_uid, _pw)

def test_post_group():

    sleep(5)
    group_link = 'https://www.facebook.com/groups/1824383134456259'
    content = 'Anh chị có nhu cầu THÊU Vi Tính nhanh chóng, đẹp, hợp túi tiền thì liên hệ xưởng bên em nhé ! Liên hệ SĐT/ZALO: 0354.777.297'


    PHOTOS_DIR = r"H:\fbtools\image\dep\*.jpg"
    photo_img = random.choices(glob.glob(PHOTOS_DIR), k=2)
    print(photo_img)

    pending_link = fb_scraper.post_group(group_link, content, photo_img)

    print('Postlink: ', pending_link)

def test_scan_group_by_keyword(keyword):
    fb_scraper.scan_group_by_keyword(keyword)



test_post_group()
# test_scan_group_by_keyword('Giày%20dép')
while True:
    if fb_scraper.is_brower_closed():
        break
    sleep(5)
