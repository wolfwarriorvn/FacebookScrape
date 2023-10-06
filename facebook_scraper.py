# -*- coding: utf-8 -*-
from constants import (
    CHROME_DRIVER,
    CHROME_PROFILES,
    FB_XPATH_ARTICLE,
    FB_XPATH_APPROVE,
    FB_XPATH_DECLINE,
    FB_XPATH_POSTER,
    FB_XPATH_SCROLLBAR,
    FB_XPATH_GROUP_LIST,
    FB_XPATH_GROUP_LINKS,
    PROXY_PATH

)
import os
import re
import pandas as pd
import time
from enum import Enum
from time import sleep
from PySide6.QtCore import QMutex
import pyotp

import utils
from utils import LogLevel, log

from random import randrange
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from subprocess import CREATE_NO_WINDOW

from selenium.common.exceptions import (
    TimeoutException,
    NoSuchWindowException,
    WebDriverException
)

class GetElement(Enum):
    ONE = 0
    MORE = 1

class GroupInfo():
    def __init__(self, name, link, category=None, members = None, details = None):
        self.name = name
        self.link = link
        self.category = category
        self.members = members
        self.details = details

class FacebookScraper:
    def __init__(self, uid, password, zip_proxy = None):
        self.uid = uid
        self.password = password

        options = webdriver.ChromeOptions()
        options.add_argument(
            r'--user-data-dir='+ CHROME_PROFILES+ fr'{self.uid}')
        # options.add_argument("--start-maximized")
        # options.add_experimental_option('excludeSwitches', ['disable-popup-blocking', 'enable-automation'])
        options.add_argument("--window-size=300,500")
        # options.add_argument("--headless --disable-gpu")
        options.add_argument("--disable-notifications")
        
        # options.add_argument("--enable-file-cookies")
        # options.add_argument(r'--profile-directory=12')

        # keep chrome tab open
        # options.add_experimental_option("detach", True)

        # login proxy
        if zip_proxy:
            # proxy_path = os.path.join(PROXY_PATH, zip_proxy + '_extension.zip')
            proxy_path = PROXY_PATH + zip_proxy + '_extension.zip'
            if os.path.exists(proxy_path):
                options.add_extension(proxy_path)

        service_obj = Service(CHROME_DRIVER)
        service_obj.creation_flags = CREATE_NO_WINDOW
        self.driver = webdriver.Chrome(service=service_obj, options=options)
        # self.driver.minimize_window()
        # self.driver.implicitly_wait(10)


        # self.driver.get("https://www.facebook.com/")
        # if self.check_login():
        #     print("Already loggin!")
        # else:
        #     raise Exception("Login {} lại nhé!!!".format(self.uid))
            # self.login_with_userpass()
    def get_cookies(self):
        return self.driver.get_cookies()
    def login_with_cookies(self, cookies):
        # self.driver.get("https://www.facebook.com/")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        sleep(5)
        self.driver.refresh()

    def check_login(self):
        self.driver.get("https://www.facebook.com/")

        # for cookie in cookies:
        #     self.driver.add_cookie(cookie)
        # print("Cookie la: ",self.driver.get_cookies())
        if self.driver.title in ['Facebook – log in or sign up', 'Facebook - log in or sign up', 'Facebook - Đăng nhập hoặc đăng ký'] :
            return False
        else:
            return True

    def login_with_userpass(self, _2fa = None):
        if self.check_login():
            print("Already loggin!")
            return
        sleep(1)
        self.driver.get("https://mbasic.facebook.com/")

        sleep(2)
        try:
            uid_input = self.driver.find_element(By.XPATH, '//*[@type="text"]')
            uid_input.send_keys(self.uid)
            sleep(1)
            password_input = self.driver.find_element(
                By.XPATH, '//*[@type="password"]')
            password_input.send_keys(self.password)
            sleep(1)
            password_input.send_keys(Keys.ENTER)
            sleep(3)

            #input 2fa code
            if _2fa is None:
                return
            input_2fa =  self.driver.find_element(By.XPATH, "//input[@type='text']")
            code_2fa = pyotp.TOTP(_2fa)
            input_2fa.send_keys(code_2fa.now())
            sleep(1)
            next_btn = self.driver.find_element(By.XPATH, "//input[@id='checkpointSubmitButton-actual-button']")
            next_btn.click()
            sleep(2)
            next_btn2 = self.driver.find_element(By.XPATH, "//input[@id='checkpointSubmitButton-actual-button']")
            next_btn2.click()
            sleep(2)

        except Exception:
            print(
                'Some exception occurred while trying to find username or password field')
    def login(self):
        try:
            uid_input = self.driver.find_element(By.XPATH, '//*[@id="email"]')
            uid_input.send_keys(self.uid)
            sleep(1)
            password_input = self.driver.find_element(
                By.XPATH, '//*[@id="pass"]')
            password_input.send_keys(self.password)
            sleep(1)
            password_input.send_keys(Keys.ENTER)
            sleep(3)
        except Exception:
            print(
                'Some exception occurred while trying to find username or password field')

    def is_brower_closed(self):
        isClosed = False
        try:
            self.driver.title
        except (WebDriverException, NoSuchWindowException) as e:
            isClosed = True
        return isClosed
    def open_url(self, url):
        self.driver.get(url)
        self.wait_fully_load()
        
        sleep(randrange(2, 5))

    def wait_fully_load(self):
        WebDriverWait(self.driver, 20).until(
            lambda wd: self.driver.execute_script(
                "return document.readyState") == 'complete',
            "Page taking too long to load"
        )

    def scroll(self, loop):
        for i in range(loop):
            self.driver.execute_script(
                'window.scrollTo(0,document.body.scrollHeight);')
            sleep(randrange(2, 5))
            self.wait_fully_load()

    def scroll_down_element(self, element, max_loop):
        max_scroll = 0
        for loop in range(0, max_loop):
            try:
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({ behavior: 'smooth', block: 'end' });", element)
                sleep(randrange(2, 5))
                self.wait_fully_load()
                actions = ActionChains(self.driver)
                actions.move_to_element(element).perform()
                scroll_height = element.get_property('scrollHeight')
                print("scroll_height: ", scroll_height)
                if (scroll_height <= max_scroll):
                    break
                max_scroll = scroll_height
            except Exception as e:
                print("lỗi là: ", e)
                break
    def scroll_down_byelement(self, element):
        max_scroll = 0
        while True:
            try:
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({ behavior: 'smooth', block: 'end' });", element)
                sleep(randrange(2, 5))
                self.wait_fully_load()
                actions = ActionChains(self.driver)
                actions.move_to_element(element).perform()
                scroll_height = element.get_property('scrollHeight')
                print("scroll_height: ", scroll_height)
                if (scroll_height <= max_scroll):
                    break
                max_scroll = scroll_height
            except Exception as e:
                print("lỗi là: ", e)
                break

    def close(self):
        try:
            self.driver.quit()
        except (WebDriverException, NoSuchWindowException) as e:
            print("Close error: ", e)
            pass    
    # def __del__(self):
        # try:
        #     self.driver.close()
        # except (WebDriverException, NoSuchWindowException) as e:
        #     pass



    def check_xpath(self, webelement, xpath, xpath_name, get_element: GetElement, timeout=10):
        try:
            # element = webelement.find_elements(By.XPATH, xpath)
            element = WebDriverWait(webelement, timeout).until(
                EC.presence_of_all_elements_located((By.XPATH, xpath)))
            if len(element) == 1:
                if get_element is GetElement.MORE:
                    return element
                return element[0]
            elif len(element) > 1:
                if get_element is GetElement.ONE:
                    # log(LogLevel.ERROR, xpath_name + " get more than one")
                    # return None
                    return element[0]
                return element
            else:
                log(LogLevel.ERROR, xpath_name + " is not found")
                return None
        except Exception as e:
            log(LogLevel.ERROR, xpath_name + " was Exception " + str(e))
            return None
        except TimeoutException as ex:
            log(LogLevel.ERROR, xpath_name + " was timeout " + str(ex))
            return None

    def get_posted_link(self, group_url):
        posted_link = None
        # group_url = 'https://www.facebook.com/groups/269277260902215/'
        # group_url = 'https://www.facebook.com/groups/1000875993405846/'
        self.open_url(group_url + 'my_posted_content')
        FB_XPATH_POSTED = "//*[@aria-label='View in group']"
        posted_link = self.check_xpath(self.driver, FB_XPATH_POSTED,
                                       "FB_XPATH_POSTED", GetElement.ONE, 1)

        if posted_link is None:
            return None
        print(posted_link.get_attribute('href'))
        href = posted_link.get_attribute('href')
        posted_id = href.split('multi_permalinks=')[1].split('&__cft__')[0]
        print(posted_id)
        return group_url+posted_id
    
    def get_post_history(self, pageid, loop_scan):
        pending_post = []
        history_url = "https://www.facebook.com/{}/allactivity?activity_history=false&category_key=GROUPPOSTS&manage_mode=false&should_load_landing_page=false".format(pageid)
        self.open_url(history_url)

        FB_XPATH_GROUPS_MAIN = "//div[@role='main']"
        group_main_element =  self.check_xpath(self.driver, FB_XPATH_GROUPS_MAIN,
                                    "FB_XPATH_GROUPS_MAIN", GetElement.ONE)
        if group_main_element is None:
            return []
        self.scroll_down_element(group_main_element, loop_scan)
        
        FB_XPATH_TODAY_POSTS = "(//div[@role='main']//a[contains(@href, 'permalink') or contains(@href, 'pending_posts')])//self::div/div/div/div[3]/span/div/div/div[2]/div/span/div/span[text()='Nhóm công khai']//ancestor::a"

        post_elements = self.check_xpath(self.driver, FB_XPATH_TODAY_POSTS,
                                    "FB_XPATH_TODAY_POSTS", GetElement.MORE)
        if post_elements is None:
            return []
        
        for post_element in post_elements:
            pending_post.append(post_element.get_attribute('href').replace('pending_posts', 'posts').replace('permalink', 'posts'))
        
        return pending_post

    def get_post_today(self, pageid):
        pending_post = []
        history_url = "https://www.facebook.com/{}/allactivity?activity_history=false&category_key=GROUPPOSTS&manage_mode=false&should_load_landing_page=false".format(pageid)
        self.open_url(history_url)

        FB_XPATH_GROUPS_MAIN = "//div[@role='main']"
        group_main_element =  self.check_xpath(self.driver, FB_XPATH_GROUPS_MAIN,
                                    "FB_XPATH_GROUPS_MAIN", GetElement.ONE)
        if group_main_element is None:
            return []
        self.scroll_down_element(group_main_element, 2)
        FB_XPATH_TODAY_POSTS = "(//div[@role='main']/div/div[2]//a[contains(@href, 'permalink') or contains(@href, 'pending_posts')])//self::div/div/div/div[3]/span/div/div/div[2]/div/span/div/span[text()='Nhóm công khai']//ancestor::a"

        post_elements = self.check_xpath(self.driver, FB_XPATH_TODAY_POSTS,
                                    "FB_XPATH_TODAY_POSTS", GetElement.MORE)
        if post_elements is None:
            return []
        
        for post_element in post_elements:
            pending_post.append(post_element.get_attribute('href').replace('pending_posts', 'posts').replace('permalink', 'posts'))
        
        return pending_post

    def check_approval_post(self, pending_post):
        self.open_url(pending_post)

        FB_XPATH_POST_PRESENCE = "//div[@aria-posinset='1']"
        try:
            element = WebDriverWait(self.driver, 0).until(EC.presence_of_element_located((By.XPATH, FB_XPATH_POST_PRESENCE)))
        except Exception as e:
            return False

        return True

    def check_group_allow_post(self, group_link):
        self.open_url(group_link)

        FB_XPATH_WRITE_POST_PRESENCE = "//*[text()='Write something...' or text()='Bạn viết gì đi...']"
        try:
            element = WebDriverWait(self.driver, 0).until(EC.presence_of_element_located((By.XPATH, FB_XPATH_WRITE_POST_PRESENCE)))
        except Exception as e:
            return False
        
        return True
    
    def like_url_posted(self, url):
        self.open_url(url)

        FB_XPATH_LIKE = "//div[@aria-label='Like' or @aria-label='Thích']"
        btn_like_element = self.check_xpath(self.driver, FB_XPATH_LIKE,
                                    "FB_XPATH_LIKE", GetElement.ONE)
        if btn_like_element is None:
            return False
        btn_like_element.click()
        self.driver.implicitly_wait(2)
        return True

    def post_group(self, group_url, contents, photos):
        post_status = False
        # url = "https://www.facebook.com/groups/1763453443938234/"
        # group_url = "https://www.facebook.com/groups/1400319690267642/"
        # group_url = utils.get_available_groups_link()[0]
        self.open_url(group_url)
        print(group_url)
        FB_XPATH_TAB_LIST = '//*[@role="tablist"]'
        tab_list = self.check_xpath(self.driver, FB_XPATH_TAB_LIST,
                                    "FB_XPATH_TAB_LIST", GetElement.ONE)

        if tab_list is None:
            return post_status
        actions = ActionChains(self.driver)
        actions.move_to_element(tab_list).perform()
        sleep(randrange(2, 5))

        FB_XPATH_WRITE_POST = "//*[text()='Write something...' or text()='Bạn viết gì đi...']"

        write_post = self.check_xpath(self.driver, FB_XPATH_WRITE_POST,
                                      "FB_XPATH_WRITE_POST", GetElement.ONE)
        if write_post is None:
            log(LogLevel.ERROR, "groups error is: " + group_url)
            return post_status
        write_post.click()
        sleep(randrange(2, 5))
        FB_XPATH_CREATE_PUBLIC_POST = '//div[@aria-label="Create a public post…" or @aria-label="Write something..." or @aria-label="Tạo bài viết công khai..."]'
        public_post = self.check_xpath(
            self.driver, FB_XPATH_CREATE_PUBLIC_POST, "FB_XPATH_CREATE_PUBLIC_POST", GetElement.ONE)
        if public_post is None:
            return post_status
        public_post.send_keys(contents)

        # FB_XPATH_TOOLBAR_LABEL = '//div[@id="toolbarLabel"]'
        # toolbar_label = self.check_xpath(self.driver, FB_XPATH_TOOLBAR_LABEL,
        #                                  "FB_XPATH_TOOLBAR_LABEL", GetElement.ONE)
        # if toolbar_label is None:
        #     return pending_link

        FB_XPATH_PHOTO_MODE = '//div[@aria-label="Ảnh/video"]'
        photo_mode = self.check_xpath(self.driver, FB_XPATH_PHOTO_MODE,
                                       "FB_XPATH_PHOTO", GetElement.ONE)
        if photo_mode is None:
            return post_status
        photo_mode.click()
        sleep(randrange(2,5))
        print(photos)

        FB_XPATH_PHOTO = "//input[@type='file' and @multiple]"

        for photo in photos:
            photo_input = self.check_xpath(self.driver, FB_XPATH_PHOTO,
                                       "FB_XPATH_PHOTO", GetElement.ONE)
            if photo_input is None:
                return post_status
            
            photo_input.send_keys(photo)
            sleep(randrange(5, 10))

        # FB_XPATH_CLOSE_POST = '//*[@aria-label="Close"]'
        # close_post = self.check_xpath(self.driver, FB_XPATH_CLOSE_POST,
        #                                 "FB_XPATH_CLOSE_POST", GetElement.ONE)
        # if close_post is None: return
        # close_post.click()
        sleep(randrange(5,10))

        FB_XPATH_POST_BTN = '//div[@aria-label="Post" or @aria-label="Đăng"]'
        post_btn = self.check_xpath(self.driver, FB_XPATH_POST_BTN,
                                    "FB_XPATH_POST_BTN", GetElement.ONE)
        if post_btn is None:
            return False
        post_btn.click()
        sleep(randrange(2, 5))


        # FB_XPATH_POST_STATUS = "//a[starts-with(@href,'https://www.facebook.com/groups/1824383134456259/pending_posts')]"

        # FB_XPATH_POST_STATUS = "//div[@role='article'][1]/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[2]/div/div[1]/span/h3/span/span/a"

        # FB_XPATH_POST_STATUS = "//div[@role='article'][1]//following::h3/span/span/a"



        # FB_XPATH_POST_STATUS = "//div[@role='article'][1]//following::span/a[starts-with(@href,'https://www.facebook.com/groups/1824383134456259/posts') or starts-with(@href,'https://www.facebook.com/groups/1824383134456259/pendin')]"
        # post_status = self.check_xpath(self.driver, FB_XPATH_POST_STATUS,
        #                             "FB_XPATH_POST_STATUS", GetElement.ONE, timeout=30)
        # if post_status:
        #     print(post_status.get_attribute('href'))
        post_status = True
        return post_status
        # post = utils.PostGroup('POSTING', group_url, '')
        # utils.update_postedfile(post, 'post')
        # utils.update_groups_report(utils.GROUPS_PATH, 'post', group_url, utils.PostStatus.PENDING, time.strftime("%Y-%m-%d %H:%M:%S"))

    def scan_group_by_keyword(self, keyword, loop_scan):
        groups = []
        url = "https://www.facebook.com/groups/search/groups/?q=" + keyword.replace(' ', '%20')
        self.open_url(url)

        FB_XPATH_GROUPS_MAIN = "//div[@role='main']"
        group_main_element =  self.check_xpath(self.driver, FB_XPATH_GROUPS_MAIN,
                                    "FB_XPATH_GROUPS_MAIN", GetElement.ONE)
        if group_main_element is None:
            return []
        self.scroll_down_element(group_main_element, loop_scan)
        
        FB_XPATH_GROUPS = "//a[@role='presentation']"
        group_elements = self.check_xpath(self.driver, FB_XPATH_GROUPS,
                                    "FB_XPATH_GROUPS", GetElement.MORE)
        if group_elements is None:
            return []
        
        for group_element in group_elements:
            g_link = group_element.get_attribute('href')
            g_name = group_element.get_attribute('innerText')

            XPATH_INFO = ".//parent::div//parent::span//parent::div//following-sibling::div[1]".format(g_link)
            group_info_element = self.check_xpath(group_element, XPATH_INFO, 'XPATH_INFO', GetElement.ONE)

            if group_info_element: 
                info_text = group_info_element.get_property('innerText')
                category, members_text, details = utils.extract_raw_group_info(info_text)

                members_in_K = members_text.replace(' thành viên', '').replace(',', '.').replace(' ', '')
                members = utils.convert_str_to_number(members_in_K)
                groups.append(GroupInfo(g_name, g_link, category, members, details))
                
        return groups

    def scan_group_of_page(self):
        groups = []
        self.open_url('https://www.facebook.com/groups/joins/?nav_source=tab&ordering=viewer_added')

        group_list = self.driver.find_elements(By.XPATH, FB_XPATH_GROUP_LIST)

        if len(group_list) == 0:
            log(LogLevel.ERROR, "FB_XPATH_SCROLLBAR is not found")
            return groups
        joined_group_list = group_list[len(group_list) - 1]


        self.scroll_down_byelement(joined_group_list)

        if len(joined_group_list.find_elements(By.XPATH, FB_XPATH_GROUP_LINKS)) == 0:
            log(LogLevel.ERROR, "FB_XPATH_GROUP_LINKS is not found")
            return groups
        joined_group_links = joined_group_list.find_elements(By.XPATH, FB_XPATH_GROUP_LINKS)

        for joined_group_link in joined_group_links:
            link = joined_group_link.get_attribute('href')

            # check valid group url:https://www.facebook.com/groups/url/
            pattern_url = r'https://\S+/$'
            if re.match(pattern_url, link):
                correct_group = joined_group_link.get_property('childElementCount')
                if correct_group == 0:
                    group_name = joined_group_link.get_attribute('innerText')
                    groups.append(GroupInfo(group_name,link))
            
        return groups

