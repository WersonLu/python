#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: if取反.py
 
@time: 2017/12/2 16:55
 
@desc:
 
'''
我 = True
if not not 我:
    print("恭喜发财")
else:
    print("捡完")

print(3 & 2)
print(bool(3>2 and 10))
print(bool(3<2 and 10)) #短路,前面错就返回错
print(bool(2>3 or 10))
