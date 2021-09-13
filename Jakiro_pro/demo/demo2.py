# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   useful
# FileName:     demo6.py
# Author:      czx
# Datetime:    2021/5/7 11:02 上午
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# --------------------------------------
import requests
from bs4 import BeautifulSoup
base_url = 'https://www.zjzfcj.com'
def main():
    url = '/book/2894/5528295.html' # 大奉

    while True:
        l = []
        r = requests.get(base_url + url)
        r.encoding = 'utf-8'
        bf = BeautifulSoup(r.text)
        text = bf.find_all('div', id='content')[0].text
        text = text.replace("　　", "\n")
        try:
            url = bf.find("a", text="下一章").attrs['href']
        except:
            url = bf.find("a", text="下一页").attrs['href']
        title = bf.find('h1', attrs='title')
        title = title.text
        for i in text.split('\n'):
            l.append(i) if i.strip() else l
        l2= []
        for i in l:
            for j in i.split("。"):
                l2.append(j.strip()) if j else l2
        for i in l2:
            continue

if __name__ == '__main__':
    main()
