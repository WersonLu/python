#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: 装饰漆.py
 
@time: 2017/12/4 13:34
 
@desc:
 
'''
import time


def gettime(go):
    stime = time.time()
    go()
    etime = time.time()
    print(etime - stime)


def go():
    lastnum = 0
    for i in range(1, 10000000):
        lastnum += 1
    print(lastnum)


gettime(go())
