#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: 再联系.py
 
@time: 2017/12/5 16:07
 
@desc:
 
'''
import os

print(os.getcwd())  # 返回脚本的路径
print(os.listdir("c:\\"))  # 返回c盘下面的文件夹

# os.remove("f:/f.txt") # 删除文件
print(os.path.split("e:/study/fileread/1.txt"))  # 分离路径和文件名
print(os.path.splitext(r"/study/fileread/2.txt"))  # 分离扩展名
print(os.path.dirname("e:/study/fileread/1.txt"))  # 获取路径名
print(os.path.basename("e:/study/fileread/1.txt"))  # 获取文件名
print(os.getenv("e:/study/fileread/1.txt"))  # 获取环境变量

import pickle

d = dict(url='index.html', title='首页', content='你好')
a = pickle.dumps(d)  # dumps 方法可以将任意对象序列化成一个str
print(a)

f = open(r'E:\study\fileread\dump.txt', 'wb')
pickle.dump(a, f)  # dump 可以将序列化的对象写入文件中
f.close()

# 反序列化方法是loads  从磁盘读取成一个str 反序列化成对象
# load 直接把文件反序列化成对象
print(os.getpid())
