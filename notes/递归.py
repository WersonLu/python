#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     递归
   Author :       aaa
   date：          2017/12/14
-------------------------------------------------
"""


def to1(n):
    if n == 0:
        return 0
    else:
        return n + to1(n - 1)


print(to1(5))  # 15


def go(num):
    if num == 0:
        return
    else:
        print("hello world  a", num - 1)  # 逆序
        go(num - 1)
        print("hello world b", num - 1)  # 是顺序


go(5)
# hello world 0
# hello world 1
# hello world 2
# hello world 3
# hello world 4
# 递归如何执行的?
# 线性递归
