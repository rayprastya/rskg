from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os

class rskgi(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('http://192.168.55.127/apprskgteaminova/index.php?r=site/login')
        self.driver.find_element_by_id('LoginForm_username').send_keys('admin')
        sleep(2)
        self.driver.find_element_by_id('LoginForm_password').send_keys('inovabdg')
        sleep(2)
        #self.driver.find_element_by_id('LoginForm_instalasi').click()
        #sleep(1)
        self.driver.find_element_by_css_selector("#LoginForm_instalasi [value='13']").click()
        sleep(1)
        #self.driver.find_element_by_id('LoginForm_ruangan').click()
        #sleep(1)
        self.driver.find_element_by_css_selector("#LoginForm_ruangan [value='1']").click()
        sleep(1)
        self.driver.find_element_by_name('yt0').click()
        sleep(1)
        self.driver.find_element_by_class_name('close').click()
        self.driver.find_element_by_class_name('shortcut4').click()
        self.driver.find_element_by_class_name('shortcut').click()
        self.driver.find_element_by_name('yt1').click()
