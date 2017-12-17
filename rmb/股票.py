#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     股票
   Author :       aaa
   date：          2017/12/15
-------------------------------------------------
"""
import re
import urllib
import urllib.request


def getpage(path):
    data = urllib.request.urlopen(path).read().decode('gbk')
    return data

def getcode():
    regex=r"<li><a target=\"_blank\" href=\"http://quote.eastmoney.com/sz300700.html\">岱勒新材(300700)</a></li>"


path = "http://quote.eastmoney.com/stocklist.html"
data = getpage(path)
print(data)
