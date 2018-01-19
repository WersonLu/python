#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2018/1/8 2:43
 
'''
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

list_a = map(lambda item: item ** 2, lst)
print(list_a)

list_b = [item ** 2 for item in lst]
print(list_b)

# 奇数平方和
list_c = [item ** 2 for item in lst if item % 2]
print(list_c)

x = 'spa'


def func():
    print(x)


# func()输出spa

def funb():
    x = 'ni'
    print(x)


# funb()
# print(x)


def fund():
    global x
    x = 'ni'
    print(x)


# fund()
# print(x)


def fune():
    x = 'ni'

    def nested():
        nonlocal x
        x = 'span'

    nested()
    print(x)


fune()
