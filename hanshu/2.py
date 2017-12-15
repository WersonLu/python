#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: 2.py
 
@time: 2017/12/2 13:36
 
@desc:
 
'''
import time

myTimes = time.time()

myTimes = int(myTimes)

print(myTimes)
myTimes = myTimes % 10  # 生成随机数
print("%", myTimes)
print(chr(ord('a') + myTimes))  # 生成随机字符
print(ord('z'))
