#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: 对象文件读写.py
 
@time: 2017/12/5 10:40
 
@desc:
 
'''
import pickle

mylist = [[1, 2, 3, 4, 5], ['abc', 'xyz', 'hello']]
file = open("1.txt", "wb")
pickle.dump(mylist, file)  # 保存list到文件
file.close()

mylist2 = []
file = open("1.txt", "wb")
mylist2 = pickle.load(file)  # 读取文件到list
print(mylist2)
