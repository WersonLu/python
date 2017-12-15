#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: 函数的属性.py
 
@time: 2017/12/4 11:56
 
@desc:
 
'''


def getMax(num1, num2):
    if num1 < num2:
        return num2
    else:
        return num1


num = getMax(100, 123)
print(num)


def go():
    print("go")


print(go())  # 没有返回值默认为None


def to():
    return 1, 2, 3


num1, num2, num3 = to()
print(num2, num1, num3)
