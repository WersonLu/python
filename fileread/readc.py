#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/8 9:56
 
'''

# file = open("C:\\Users\\wersonliu\\Desktop\\new.txt", 'w')
# mystr = "hello python 中国"
# file.write(mystr) # 自动转码,系统指定 默认中文环境gbk
# print("写完")
# file.close()
file = open("C:\\Users\\wersonliu\\Desktop\\new.txt", 'r')
mystr = file.read()  # read不能指定编码,使用系统默认,读取转换utf-8
print(mystr)
file.close()
