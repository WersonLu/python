#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: get.py
 
@time: 2017/12/6 10:07
 
@desc:
 
'''
import requests

user_agent = '(Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
headers = {'User-Agent': user_agent}
cookies = dict(name='qiye', age='10')  # 自定义cookie发送出去
r = requests.get('http://www.baidu.com', headers=headers, cookies=cookies)
print(r.text)  #
# for cookie in r.cookies.keys():
#     print(cookie+':'+r.cookies.get(cookie))   # 可以获取响应中的cookie值

# BAIDUID:1ABFD32B8EFFA95C6E7904655B2D16F7:FG=1
# BIDUPSID:1ABFD32B8EFFA95C6E7904655B2D16F7
# H_PS_PSSID:25249_1451_24867_21088_18560_17001_25178_23384_20719
# PSTM:1512528454
# BDSVRTM:0
# BD_HOME:0

a = requests.get('http://github.com')
print(a.url)
print(a.status_code)
print(a.history)

