#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: 文件指针.py
 
@time: 2017/12/5 10:17
 
@desc:
 
'''

file = open("3.txt", "r")
print(file.tell())  # 0
# mystr = file.readline()  # 读取英文，遇到换行符
mystr2=file.read()
# print(mystr)
print(mystr2)
# print(len(mystr))  # 15
print(file.tell())  # 15+'\n'  获取文件指针的位置，
file.close()
