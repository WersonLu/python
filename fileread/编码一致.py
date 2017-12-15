#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/8 10:15
 
'''
file = open("C:\\Users\\wersonliu\\Desktop\\newx.txt", 'w')
mystr = "hello python 中国"
file.write(mystr) # 自动转码,系统指定 默认中文环境gbk
print("写完")
file.close()
