# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Jakiro_pro
# FileName:     HJ53.py
# Author:      Jakiro
# Datetime:    2021/7/20 19:41
# Description: 杨辉三角变形
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


while True:
    try:
        a = int(input())
        if a <= 2:
            print(-1)
        elif a % 2 == 1:
            print(2)
        elif a % 4 == 0:
            print(3)
        else:
            print(4)
    except:
        break