#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: 算学费.py
 
@time: 2017/12/4 9:59
 
@desc:
 
'''
money = 10000
year = 1
while year < 11:
    money = money * 1.05
    year = year + 1
lastmoney = money
year = 1
while year < 4:
    money = money * 1.05
    year = year + 1
    lastmoney += money
print(lastmoney)
