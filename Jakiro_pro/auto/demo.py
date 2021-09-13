# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Jakiro_pro
# FileName:     demo.py
# Author:      Jakiro
# Datetime:    2021/8/26 15:00
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import os
import time

dirver = webdriver.Chrome("/Users/qiujie/Documents/tools/chromedriver")

dirver.get('https://139.196.252.185:25601/management/application/add')

dirver.implicitly_wait(10)
dirver.maximize_window()
dirver.find_element_by_id('details-button').click()
dirver.find_element_by_id('proceed-link').click()
dirver.find_element_by_xpath("//input[@placeholder='请输入邮箱']").send_keys('luhaotian1@zhuozhuo.io')
dirver.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys('Aa111111+')
dirver.find_element_by_xpath("//button[@class='btn']").click()

a = os.popen('kmg 2fa ANTJLIQCPCAFCVIQTQ7NPY7KAHGF4EPR').read()

dirver.find_element_by_id('id-0').send_keys(a)

dirver.find_element_by_xpath("//div [@class='icon icon_application_management']").click()

dirver.find_element_by_xpath("//*[contains(text(),'添加SDP应用')]").click()
dirver.find_element_by_xpath("//span[@class='icon_fold expend']").click()
time.sleep(1)
dirver.find_element_by_css_selector('[class="sdp-button-content"]').click()

dirver.find_element_by_xpath("//input[@placeholder='请输入应用名称']").send_keys('测试服务应用')
dirver.find_element_by_xpath("//input[@placeholder='请输入该服务名称']").send_keys('测试服务')
dirver.find_element_by_xpath("//div[@class='placeholder']").click()
dirver.find_element_by_xpath("//*[contains(text(),'HTTPS')]").click()
dirver.find_element_by_xpath(
    "/html/body/div[1]/div[1]/div[3]/div[2]/div/div/div[4]/div[1]/div/div[3]/div[1]/div[1]/div[1]/input").send_keys(
    '10.10.6.6')

# time.sleep(1)
# ActionChains(dirver).double_click(dirver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/div[2]/div/div/div[4]/div[1]/div/div[3]/div[1]/div[3]/input")).perform()
# time.sleep(1)\ue003

''' 
上面的代码是进入添加SDP应用页面
'''

ac = ActionChains(dirver)
time.sleep(3)

# 找到ip输入框元素
# ele_n = dirver.find_element_by_xpath(
#     "//*[@id='app']/div[1]/div[3]/div[2]/div/div/div[4]/div[1]/div/div[3]/div[1]/div[1]/div[1]/input")

# 找到端口的输入框元素
ele_n = dirver.find_element_by_xpath(
    '//*[@id="app"]/div[1]/div[3]/div[2]/div/div/div[4]/div[1]/div/div[3]/div[1]/div[3]/input')

# 鼠标点击一下输入框
ac.click(ele_n).perform()

# 鼠标双击一下输入框
ac.double_click(ele_n).perform()

time.sleep(3)
# 输入框输入5
ele_n.send_keys('5')

time.sleep(3)
# 通过键盘删除元素
ele_n.send_keys(Keys.BACKSPACE)

time.sleep(5)
dirver.quit()
