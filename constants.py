# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 15:38:38 2022

@author: vietc
"""

POST_NUMBER = 2
DEFAULT_PROFILES = "D:\Python\FB_GUI_TEMP\profiles.txt"
DEFAULT_PROFILES_CSV = "D:\Python\FB_GUI_TEMP\profiles.csv"
PROXY_DEFAULT = "D:\Python\FB_GUI_TEMP\proxy\proxy.csv"
PROXY_PATH = r"H:\\fbtools\\proxy\\"

PHOTOS_DIR = r"D:\Python\PhotoLibrary\*.jpg"
SHOES_PHOTOS_DIR = r"D:\Python\PhotoLibrary\Shoes\*.jpg"
CLOTHES_PHOTOS_DIR = r"D:\Python\PhotoLibrary\Clothes\*.jpg"
GROUPS_PATH = r"G:\My Drive\FBSCRAP\log\group_tita.xlsx"

##########################################################################################
################################# FBscrape setting #######################################
##########################################################################################
CHROME_DRIVER = "H:\\fbtools\\chromedriver\\chromedriver.exe"
CHROME_PROFILES = "H:\\fbtools\\ChromeProfiles\\"

# FB_XPATH_ARTICLE = "//div[@role='article']"
FB_XPATH_ARTICLE = "//div[@aria-posinset]"

# FB_XPATH_SHARE_LINK = ".//h4[@*]"
FB_XPATH_APPROVE = ".//div[@aria-label='Phê duyệt' or @aria-label='Approve']"
FB_XPATH_DECLINE = ".//div[@aria-label='Từ chối' or @aria-label='Decline']"
FB_XPATH_POSTER = ".//h3[starts-with(@id,'jsc_c_')]"


FB_XPATH_GROUP = '//div[@aria-label="List of groups"]'
FB_GROUP_TAB = "//div[@aria-label='List of groups']"
FB_XPATH_SCROLLBAR = "//div[@aria-label='Preview of a group']"
FB_XPATH_GROUP_LINKS = "//a[starts-with(@href,'https://www.facebook.com/groups/')]"
