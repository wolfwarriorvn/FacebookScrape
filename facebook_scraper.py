# -*- coding: utf-8 -*-
from constants import (
    CHROME_DRIVER,
    CHROME_PROFILES,
    FB_XPATH_ARTICLE,
    FB_XPATH_APPROVE,
    FB_XPATH_DECLINE,
    FB_XPATH_POSTER,
    FB_GROUP_TAB,
    FB_XPATH_GROUP,
    FB_XPATH_SCROLLBAR,
    FB_XPATH_GROUP_LINKS,
    PROXY_PATH

)
import os
import re
import pandas as pd
import time
from enum import Enum
from time import sleep

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


class FacebookScraper:
    def __init__(self, uid, password, zip_proxy = None):
        self.uid = uid
        self.password = password
        options = webdriver.ChromeOptions()
        options.add_argument(
            r'--user-data-dir='+ CHROME_PROFILES+ fr'{self.uid}')
        options.add_argument("--start-maximized")
        options.add_argument("--start-maximized")
        # options.add_argument(r'--profile-directory=12')

        # keep chrome tab open
        options.add_experimental_option("detach", True)

        # login proxy
        if zip_proxy:
            # proxy_path = os.path.join(PROXY_PATH, zip_proxy + '_extension.zip')
            proxy_path = PROXY_PATH + zip_proxy + '_extension.zip'
            if os.path.exists(proxy_path):
                options.add_extension(proxy_path)

        service_obj = Service(CHROME_DRIVER)
        service_obj.creation_flags = CREATE_NO_WINDOW
        self.driver = webdriver.Chrome(service=service_obj, options=options)

        if self.check_login():
            print("Already loggin!")
        else:
            self.login()

    def check_login(self):
        self.driver.get("https://www.facebook.com")
        if 'Facebook – log in or sign up' in self.driver.title:
            return False
        else:
            return True

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

    def __del__(self):
        try:
            self.driver.close()
        except (WebDriverException, NoSuchWindowException) as e:
            pass



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

    def post_group(self, group_url, contents, photos):
        # url = "https://www.facebook.com/groups/1763453443938234/"
        # group_url = "https://www.facebook.com/groups/1400319690267642/"
        # group_url = utils.get_available_groups_link()[0]
        self.open_url(group_url)
        print(group_url)
        FB_XPATH_TAB_LIST = '//*[@role="tablist"]'
        tab_list = self.check_xpath(self.driver, FB_XPATH_TAB_LIST,
                                    "FB_XPATH_TAB_LIST", GetElement.ONE)

        if tab_list is None:
            return False
        actions = ActionChains(self.driver)
        actions.move_to_element(tab_list).perform()
        sleep(randrange(2, 5))

        FB_XPATH_WRITE_POST = "//*[text()='Write something...' or text()='Bạn viết gì đi...']"

        write_post = self.check_xpath(self.driver, FB_XPATH_WRITE_POST,
                                      "FB_XPATH_WRITE_POST", GetElement.ONE)
        if write_post is None:
            log(LogLevel.ERROR, "groups error is: " + group_url)
            return False
        write_post.click()
        sleep(randrange(2, 5))
        FB_XPATH_CREATE_PUBLIC_POST = '//div[@aria-label="Create a public post…" or @aria-label="Write something..."]'
        public_post = self.check_xpath(
            self.driver, FB_XPATH_CREATE_PUBLIC_POST, "FB_XPATH_CREATE_PUBLIC_POST", GetElement.ONE)
        if public_post is None:
            return False
        public_post.send_keys(contents)

        FB_XPATH_TOOLBAR_LABEL = '//div[@id="toolbarLabel"]'
        toolbar_label = self.check_xpath(self.driver, FB_XPATH_TOOLBAR_LABEL,
                                         "FB_XPATH_TOOLBAR_LABEL", GetElement.ONE)
        if toolbar_label is None:
            return False

        FB_XPATH_PHOTO = '..//input[@type="file"]'
        photo_input = self.check_xpath(toolbar_label, FB_XPATH_PHOTO,
                                       "FB_XPATH_PHOTO", GetElement.ONE)
        if photo_input is None:
            return False
        for photo in photos:
            photo_input.send_keys(photo)
            sleep(randrange(2, 5))

        # FB_XPATH_CLOSE_POST = '//*[@aria-label="Close"]'
        # close_post = self.check_xpath(self.driver, FB_XPATH_CLOSE_POST,
        #                                 "FB_XPATH_CLOSE_POST", GetElement.ONE)
        # if close_post is None: return
        # close_post.click()
        # sleep(randrange(2,5))

        FB_XPATH_POST_BTN = '//div[@aria-label="Post"]'
        post_btn = self.check_xpath(self.driver, FB_XPATH_POST_BTN,
                                    "FB_XPATH_POST_BTN", GetElement.ONE)
        if post_btn is None:
            return False
        post_btn.click()
        sleep(randrange(2, 5))
        
        return True
        # post = utils.PostGroup('POSTING', group_url, '')
        # utils.update_postedfile(post, 'post')
        # utils.update_groups_report(utils.GROUPS_PATH, 'post', group_url, utils.PostStatus.PENDING, time.strftime("%Y-%m-%d %H:%M:%S"))

    def scan_group_of_page(self):
        status = False
        group_link_text = []
        self.open_url('https://www.facebook.com/groups/joins/?nav_source=tab&ordering=viewer_added')

        if len(self.driver.find_elements(By.XPATH, FB_XPATH_SCROLLBAR)) == 0:
            log(LogLevel.ERROR, "FB_XPATH_SCROLLBAR is not found")
            return status,group_link_text
        group_tab = self.driver.find_element(By.XPATH,FB_XPATH_SCROLLBAR)

        self.scroll_down_byelement(group_tab)

        if len(group_tab.find_elements(By.XPATH, FB_XPATH_GROUP_LINKS)) == 0:
            log(LogLevel.ERROR, "FB_XPATH_GROUP_LINKS is not found")
            return status,group_link_text
        group_links = group_tab.find_elements(By.XPATH, FB_XPATH_GROUP_LINKS)

        for group_link in group_links:
            link = group_link.get_attribute('href')

            # check valid group url:https://www.facebook.com/groups/url/
            pattern_url = r'https://\S+/$'
            if re.match(pattern_url, link):
                group_link_text.append(link)

        if group_link_text:
            status = True
        return status,group_link_text
        # utils.write_textfile("group_links.txt", group_link_text)

