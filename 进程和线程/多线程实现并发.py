#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     多线程实现并发
   Author :       aaa
   date：          2017/12/15
-------------------------------------------------
"""
import win32api
import _thread


def show(num):
    win32api.MessageBox(0, "xxxx", "啊啊啊", 0)


# 顺序执行
# for i in range(6):
#     show()

for i in range(5):
    _thread.start_new_thread(show,(i,))
show(6)
