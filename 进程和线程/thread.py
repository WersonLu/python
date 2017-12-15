#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: thread.py
 
@time: 2017/12/5 17:27
 
@desc:
 
'''
import random
import time, threading


# 新线程执行的代码：
def thread_run(urls):
    print('Current %s is running...' % threading.current_thread().name)

    for url in urls:
        print('%s ---->>> %s' % (threading.current_thread().name, url))

        time.sleep(random.random())
    print('%s ended.' % threading.current_thread().name)


print('%s is running...' % threading.current_thread().name)

t1 = threading.Thread(target=thread_run, name='Thread_1', args=(['url_1', 'url_2', 'url_3'],))

t2 = threading.Thread(target=thread_run, name='Thread_2', args=(['url_4', 'url_5', 'url_6'],))
t1.start()
t2.start()
t1.join()
t2.join()
print('%s ended.' % threading.current_thread().name)
#创建线程的两种方法

# 把函数传入并创建Thread 实例,然后调用start方法开始执行

# 从threading.Thread 继承并创建线程类,从写__init__ 和run方法
