# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Jakiro_pro
# FileName:     demo2.py
# Author:      Jakiro
# Datetime:    2021/8/26 15:45
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import os
import time
driver = webdriver.Chrome("/Users/qiujie/Documents/tools/chromedriver")
ac = ActionChains(driver)
try:
    driver.get(r'https://www.baidu.com/')
    input_ele = driver.find_element_by_id('kw')
    input_ele.send_keys('aaa')
    time.sleep(3)
    ac.double_click(input_ele).perform()
    time.sleep(3)
    input_ele.send_keys(Keys.BACKSPACE)
finally:
    time.sleep(3)
    driver.quit()