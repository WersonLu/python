#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/15 16:12
 
'''
import threading
import time


def go1():
    with cond:
        for i in range(1, 10, 2):
            time.sleep(1)
            print(threading.current_thread().name, i)
            cond.notify()
            cond.wait()


def go2():
    with cond:
        for i in range(0, 11, 2):
            time.sleep(1)
            print(threading.current_thread().name, i)
            cond.wait()
            cond.notify()



cond = threading.Condition()  # 线程条件变量
threading.Thread(target=go2).start()
threading.Thread(target=go1).start()
# Thread-1 0
# Thread-2 1
# Thread-1 2
# Thread-2 3
# Thread-1 4
# Thread-2 5
# Thread-1 6
# Thread-2 7
# Thread-1 8
# Thread-2 9
# Thread-1 10