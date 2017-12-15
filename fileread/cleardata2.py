#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/8 10:30
 
'''

filepath = r"E:\study\fileread\kf.txt"
file = open(filepath, "rb")  # 按照指定编码
for line in file:
    linstr = line.decode("utf-8")
    mylist = linstr.split(" ")
    print(mylist)
file.close()
