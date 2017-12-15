#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: eval-exec.py
 
@time: 2017/12/4 15:48
 
@desc:
 
'''
i = []
i.append('item')
print(i)
print(repr(i))
print(eval("12.7"))
print("hello")  # 用于多行
print('hello')  # 用于单个
print("""hello""")  #
print("abac\ncdf")  # 换行

print("abc".upper())
print(max("asasa"))

print(" a  ac".strip())  # 前后去空格

mystr = "as323 # fwe2 # wer1"
ml = mystr.split("#")
print(ml)


