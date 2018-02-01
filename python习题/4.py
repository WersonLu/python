#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-29 12:22:17
# @Author  : wersonliu (${email})
# @Link    : ${link}
# @Version : $Id$

# print(range(5, -5, 1))
# print(range(5, -5, -1))
#
# L = [1, 2, 3, 4, 5]
# for x in L:
#     x += 1
# for i in range(len(L)):
#     L[i]+=1
#     # print(L)
# print(L)
from functools import reduce

x = 99


def func1():
    global x
    print(x)
    x = 88
    print(x)


func1()


def f1():
    x = 77

    def f2():
        print(x)

    f2()


f1()


def f3():
    x = 33

    def f4():
        print(x)

    return f4()


action = f3()
action


# def mark(N):
#     def ap(x):
#         return x ** N
#
#     return ap()
#
#
# g = mark(3)
# print(g)

# 函数式编程工具

filter() # 参数为函数和可迭代对象
reduce #py3  中移除
