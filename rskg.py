from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import pandas_datareader.data as web
import datetime as dt
from time import sleep
import os

class rskgi(object):
    def __init__(self,antrian):
        self.driver = webdriver.Chrome()
        self.antrian =  antrian
        
    def login(self):
        self.driver.get('http://192.168.55.127/ehospitalrskg/index.php?r=site/login')
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
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="yw0"]/div/a').click()

    def ambil_antrian(self):
        self.driver.find_element_by_class_name('shortcut4').click()
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div/div/a[1]').click()

        if self.antrian == "1":
            self.driver.find_element_by_name('yt0').click()
            print("")
            print("anda telah terdaftar dalam antrian hemodialisa")

        elif self.antrian == "2":
            self.driver.find_element_by_name('yt1').click()
            print("")
            print("anda telah terdaftar dalam antrian poliklinik")

        else:
            print("maaf pilihan antrian anda tidak terdaftar disini")
    
    def cek_urutan(self):
        self.driver.find_element_by_class_name('shortcut4').click()
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div/div/a[2]').click()
        hm = ()
        pn = ()
        tg = "h"
        while True:
            try:
                hm = self.driver.find_element_by_xpath('//*[@id="loket_1"]/div[2]').text
                pn = self.driver.find_element_by_xpath('//*[@id="loket_2"]/div[2]').text
                if hm == tg or pn == tg :
                    pass
                elif hm != tg:
                    print(hm)
                    #print(judul)
                    tg = hm
                    #use or!!
                elif pn != tg:
                    print(pn)
                    #print(judul)
                    tg = pn
                    #use or!!
                else:
                    print("ada yang salah ni")
                    
                
            except:
                print("hemo salah")
    

    def upload_exc(self):
        start = dt.datetime(2020,9,7)
        end = dt.datetime.today()

        df = web.DataReader ('yahoo', start, end)

        filename = "rekapdata.xlsx"
        df.to_excel(filename)
        