#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/15 17:19
 
'''

import requests
from bs4 import BeautifulSoup

# for i in range(2):
path = "https://www.alibaba.com/products/F0/keyboard/2.html"
html = requests.get(path).text
soup = BeautifulSoup(html, 'html.parser')
results = soup.find_all(class_="item-content")
for n in results:
    content = n.get_text()
    print(content)
