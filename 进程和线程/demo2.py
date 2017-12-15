#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: demo2.py
 
@time: 2017/12/5 16:52
 
@desc:
 
'''
from multiprocessing import Pool
import os, time, random


def run_task(name):
    print('我%s(pid=%s) 正在跑' % (name, os.getpid()))

    time.sleep(random.random() * 3)
    print('我%s结束' % name)


if __name__ == '__main__':
    print('当前%s' % os.getpid())
    p = Pool(processes=3)  # 创建3进程池

    for i in range(5):  # 依次向池中添加5个任务
        p.apply_async(run_task, args=(i,))  # 一开始只能运行三个任务,当一个结束,加入第四个第五个
        print('等待所有的进程跑完')  # 加进来的任务交给原先的进程在执行
        p.close()  # 任务结束关闭进程
        p.join()  # 加入新的任务
