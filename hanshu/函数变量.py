#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: 函数变量.py
 
@time: 2017/12/4 13:11
 
@desc:
 
'''


def add(num1, num2):
    return num1 + num2


def Test(go, num1, num2):  # 接口
    return go(num1, num2)


# print(Test(add, 2, 8))


def Test():
    num = 10

    def Testin():
        # nonlocal num  # 引用外部变量用于函数嵌套
        # global num 这个在这里不起作用
        num = 100
        print(num)

    Testin()
    print(num)


Test()
