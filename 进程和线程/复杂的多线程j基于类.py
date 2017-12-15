#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     复杂的多线程j基于类
   Author :       aaa
   date：          2017/12/15
-------------------------------------------------
"""

import time
import _thread
import threading

import win32api


class Mythread(threading.Thread):  # 继承
    def run(self):  # 重写
        win32api.MessageBox(0, "xxxx", "啊啊啊", 0)  # 系统,内容,标题,按钮个数


for i in range(5):
    t = Mythread()  # 初始化
    t.start()  # 开启
    t.join()  # 主线程等待线程t完成

# while True:  # 阻塞主线程
#     pass
