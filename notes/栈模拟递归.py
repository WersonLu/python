#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     栈模拟递归
   Author :       aaa
   date：          2017/12/14
-------------------------------------------------
"""


def add(num):
    if num == 0:
        return 0
    else:
        return num + add(num - 1)


print(add(5))
# 模拟栈,先进先出
mystrack = []
lastdata = 0
mystrack.append(5)
while len(mystrack) != 0:
    data = mystrack.pop()  # 弹出
    print(data)
    lastdata += data
    if data == 0:
        break
    else:
        mystrack.append(data - 1)
print(lastdata)
