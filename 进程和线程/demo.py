#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: demo.py
 
@time: 2017/12/5 16:44
 
@desc:
 
'''

import os
from multiprocessing import Process


def run_proc(name):
    print('Child progress %s (%s) Running' % (name, os.getpid()))


if __name__ == '__main__':
    print('parent process %s.' % os.getpid())

    for i in range(5):
        p = Process(target=run_proc, args=(str(i),))
        print('进程将开始')
        p.start()
    p.join()
    print('进程结束')
