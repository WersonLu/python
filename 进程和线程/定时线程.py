#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/16 11:32
 
'''

import time
import os
import threading


# i = 0
# while True:
#     time.sleep(1)
#     print("第", i, "秒")
#     i += 1

def go():
    os.system("notepad")


time1 = threading.Timer(5, go)

time1.start()
i = 0
while True:
    time.sleep(1)
    print(i)
    i += 1
