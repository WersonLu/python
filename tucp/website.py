#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/15 15:05
 
'''
import urllib.request

# 新建字典
try:

    data = urllib.request.urlopen("http://www.qinghuabeida.cn/Webadmin").read()
    print(data)
    print("页面存在")
except:
    print("页面不存在")
