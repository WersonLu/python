#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: read1.py
 
@time: 2017/12/5 9:38
 
@desc:
 
'''
file = open("2.txt", "r", encoding='utf-8')
# print(file.read(2))
# print(file.readline(),end="")
# print(file.readlines()) #读多行 成列表

for line in file:
    print(line, end="")
file.close()
