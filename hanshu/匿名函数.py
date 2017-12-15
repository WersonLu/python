#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: 匿名函数.py
 
@time: 2017/12/4 14:30
 
@desc:
 
'''
# 匿名函数关键字lambda
num = lambda a, b: a + b
print(num(1, 2))
print((lambda a, b: a + b)(100, 288))
(lambda mys: print(mys))("hello")

num3 = lambda a, b, c: a + b + c
print(num3(1, 2, 5))
