#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/9 16:24
 
'''
import threading
import random
import time

import threading
import random
import time


class MyThread(threading.Thread):
    def __init__(self, threadName, event):
        threading.Thread.__init__(self, name=threadName)
        self.threadEvent = event


def run(self):
    print("%s is ready" % self.name)
    self.threadEvent.wait()
    print("%s run!" % self.name)


sinal = threading.Event()
for i in range(10):
    t = MyThread(str(i), sinal)
    t.start()
time.sleep(1)
sinal.set()
