#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: math.py
 
@time: 2017/12/2 14:46
 
@desc:
 
'''
import math

print(abs(-6))
print(math.sqrt(9))
print(chr(26551))
print("\u5655")  # \u统一码
print("hello""")
print("hello\"\'")
# 转义字符

print("a", end="")
print("a")
# 不换行

print(1,2,4,sep="#")

import os
mystr="note"
mystr2="pad"
mystr3="D:\\study\\01.txt"
os.system(mystr+mystr2+""+mystr3)
