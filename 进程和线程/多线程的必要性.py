#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     多线程的必要性
   Author :       aaa
   date：          2017/12/15
-------------------------------------------------
"""
# import win32api   # 系统函数
import win32com
import _thread
# win32api.MessageBox(0, "xxxx", "啊啊啊", 0) # 系统,内容,标题,按钮个数

import time


def go():
    for i in range(10):
        print(i, "===")
        time.sleep(1)


for n in range(4):
    go()  # 非常慢打印结束需要40多秒
print("结束")

for i in range(4):
    # 采用多线程  用死循环阻塞线程防止主线程挂掉
    _thread.start_new_thread(go, ())  # 非常快,打印结束只需不到1秒
print("结束")
