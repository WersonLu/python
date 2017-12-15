#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     栈模拟遍历文件
   Author :       aaa
   date：          2017/12/14
-------------------------------------------------
"""
import os

path = "F:\\workspace"
# 还可以用队列 deque([])
# 队列插入一样,取出用poplift()
mystrack = []
mystrack.append(path)
with len(mystrack) != 0:
    path = mystrack.pop()  # 取出一个
    filelist = os.listdir(path)  # 遍历
    for filename in filelist:
        filepath = os.path.join(path, filename)  # 是、绝对路径
        if os.path.isdir(filepath):
            print('文件夹', filename)
            mystrack.append(filepath)
        else:
            print('文件', filename)
