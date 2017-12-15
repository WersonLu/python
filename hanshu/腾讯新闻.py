#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: 腾讯新闻.py
 
@time: 2017/12/4 9:49
 
@desc:
 
'''
import requests
from bs4 import BeautifulSoup

url = "http://news.qq.com/"
wbdata = requests.get(url).text
soup = BeautifulSoup(wbdata, 'lxml')
new_titles = soup.select("div.text>em.f14>a.linkto")

for n in new_titles:
    title = n.get_text()
    link = n.get("href")
    data = {
        '标题': title,
        '链接': link
    }
    print(data)
