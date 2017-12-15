#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/15 15:57
 
'''
import threading

import time


def goevent():
    e = threading.Event()  # 事件

    def go():
        for i in range(10):
            e.wait()  # 等待
            e.clear()  # 重置
            print(i, "go")

    threading.Thread(target=go).start()
    return e


t = goevent()

for i in range(10):
    time.sleep(i)
    t.set()  # 通知
#
# 0 go
# 1 go
# 2 go
# 3 go
# 4 go
# 5 go
# 6 go
# 7 go
# 8 go
# 9 go
