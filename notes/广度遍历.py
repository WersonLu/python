#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     广度遍历
   Author :       aaa
   date：          2017/12/15
-------------------------------------------------
"""
import os
from collections import deque

path = r"D:\Anaconda3"
queue = deque([])  # 队列
queue.append(path)
while len(queue) != 0:
    path = queue.popleft()  # 取出拉出的值
    filelist = os.listdir(path)  # 遍历路径
    for filename in filelist:
        filepath = os.path.join(path, filename)

        if os.path.isdir(filepath):
            print("文件夹", filename)
            queue.append(filepath)
        else:
            print("文件", filename)
