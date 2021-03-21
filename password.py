#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 12:08:27 2021

@author: yuanke.tsai
"""

password = 'a1234'
remain_c = 3
while remain_c > 0:
    pass_w = input('請輸入密碼：')
    if pass_w == password:
        print('登入成功！')
        break
    remain_c = remain_c - 1
    while remain_c >= 0:
        if remain_c > 0:
            print('try again! remain chance:', remain_c)
            break
        else:
            print('try later!')
            break