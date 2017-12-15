#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: money.py
 
@time: 2017/12/2 16:03
 
@desc:
 
'''
money = input("输入金额")
print(money)

print(int(eval(money), 2), "元")
print(int(round(eval(money), 2) * 10) % 10, "角")
print(int(round(eval(money), 2) * 100) % 10, "分")
