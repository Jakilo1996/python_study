# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Jakiro_pro
# FileName:     HJ55.py
# Author:      Jakiro
# Datetime:    2021/7/20 20:40
# Description: 挑7   输出7有关数字的个数，包括7的倍数，还有包含7的数字（如17，27，37...70，71，72，73...）的个数（一组测试用例里可能有多组数据，请注意处理）
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

while True:
    try:
        a = int(input())
        list1 = []
        num = 0
        for i in range(7, a + 1, 7):
            if i % 7 == 0:
                list1.append(i)
                num +=1
        print(list1)
        for i in range(7, a + 1, 10):
            if '7' in str(i) and i not in list1:
                num += 1
        print(num)
    except:
        break


