#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/15 16:54
 
'''

import threading
import queue
import time
import random

myqueue = queue.Queue(10)  # 最大容量


# 生产行为
class createThread(threading.Thread):
    def __init__(self, index, myqueue):
        threading.Thread.__init__(self)
        self.index = index
        self.myqueue = myqueue

    def run(self):
        while True:
            time.sleep(3)
            num = random.randint(1, 100000)  # 随机产品
            self.myqueue.put("生产者" + str(self.index) + "生产的玩具车编号为" + str(num))
            print(" 生产者" + str(self.index) + "玩具车" + str(num))
        self.myqueue.task_done()


# 消费行为
class buyerThread(threading.Thread):
    def __init__(self, index, myqueue):
        threading.Thread.__init__(self)
        self.index = index
        self.myqueue = myqueue

    def run(self):
        while True:
            time.sleep(1)
            item = self.myqueue.get()  # 模拟的消费行为
            if item is None:
                break
            print("客户", self.index, "购买物品为", item)


for i in range(3):
    createThread(i, myqueue).start()
for i in range(8):
    buyerThread(i, myqueue).start()
