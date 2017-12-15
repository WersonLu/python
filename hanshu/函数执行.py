#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: 函数执行.py
 
@time: 2017/12/4 12:20
 
@desc:
 
'''


def go1():
    print("go1 start")
    go2()
    print("go1 end")


def go2():
    print("go2 start")
    go3()
    print("go2 end")


def go3():
    print("go3 start")
    print("go3 end")


go1()
# 瀑布执行至上而下.
# 函数调用必须等函数返回了才能执行下一步
