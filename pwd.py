# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


password = 'a1234'
remain_c = 3
while remain_c > 0:
    pass_w = input('請輸入密碼：')
    if pass_w == password:
        print('登入成功！')
        break
    remain_c = remain_c - 1
    if remain_c > 0:
            print('try again! remain chance:', remain_c)
    elif remain_c == 0:
        print('try later!')
        break