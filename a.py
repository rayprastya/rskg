from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os
driver = webdriver.Chrome()

driver.get('https://www.youtube.com/watch?v=JwWMpspzcg8')
ch1 = ()
ch2 = "h"
while True:
    try:
        ch1 = driver.find_element_by_xpath('//*[@id="text"]/a').text
        judul = driver.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string').text
        if ch1 == ch2 :
            pass
        else:
            print(ch1)
            print(judul)
            ch2 = ch1
            #use or!!
        
    except:
        print("salaj anjeng")

            
