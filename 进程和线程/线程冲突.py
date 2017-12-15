#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     线程冲突
   Author :       aaa
   date：          2017/12/15
-------------------------------------------------
"""
import _thread
import time

num = 0


def add():
    global num
    for i in range(1000000):
        num += 1
    print(num)


# for i in range(3):
#     add()   =>3000000

for i in range(4):
    _thread.start_new_thread(add, ())  # =>2793235  此时线程冲突。

while True:
    pass
