#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/8 13:41
 
'''
import pickle

sfzlist = []
file = open("sfz.bin", "rb")
sfzlist = pickle.load(file)  # 把对象文件加载到内存
file.close()
print(sfzlist)
