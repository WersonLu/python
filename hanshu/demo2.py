#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: demo2.py
 
@time: 2017/12/2 12:18
 
@desc:
 
'''
str1="calc"
str2="calc"

print(id(str1),id(str2))

str3=str2
print(id(str1),id(str3))
num=None
print(id(num))
num=str1
print(id(num))
print(num)
