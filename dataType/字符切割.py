#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: 字符切割.py
 
@time: 2017/12/4 16:09
 
@desc:
 
'''
mystr = """
日照香炉生紫烟，遥看瀑布挂前川。
飞流直下三千尺，疑是银河落九天。
"""
mylist = mystr.splitlines()
for data in mylist:
    print(data)

m = [1, 2, 3, 4, 5, 67, 8]
for i in range(len(m)):
    if m[i] == 4:
        del m[i]  # 删除元素要终止循环
        break
print(m)
# my=m
# my[5]=888
# print(my)        浅复制
# print(m)      元素同一地址，一变都变
at = m.copy()
at[4] = 444
print(at)  # 深复制
print(m)  # 元素不同地址，一边不会影响

# 与之对应，元组在内存地址中是常量
mytumple=1,2,3,4
print(mytumple.count(1))
