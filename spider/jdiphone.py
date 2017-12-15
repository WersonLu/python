#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: jdiphone.py
 
@time: 2017/12/4 17:42
 
@desc:
 
'''
import re
import pandas as pd
import requests

f = open('f:/iphone.txt', 'a')
for i in range(0, 50):
    try:
        response = requests.get(
            'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv4962&productId=5089225&score=0&sortType=5&page=' + str(
                i) + '&pageSize=10&isShadowSku=0&rid=0&fold=1')
        response = response.text
        pat = '"content":"(.*?)","'
        res = re.findall(pat, response)
        for i in res:
            i = i.replace('\\n', '')
        f.write(i)

        f.write('\n')
        print('第' + str(i) + '写完')
    except:
        print('第' + str(i) + '出问题')
        continue
f.close()
