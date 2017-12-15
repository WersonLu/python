#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: 换行.py
 
@time: 2017/12/4 10:37
 
@desc:
 
'''
count=1
for i in range(100, 1000 + 1):
    if i % 5 == 0 and i % 6 == 0:
        print(i,end=" ")
        if count%10==0:
            print("")
        count+=1