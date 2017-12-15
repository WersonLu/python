#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/6 13:23
 
'''
import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.baidu.com").content
soup = BeautifulSoup(response, 'lxml', from_encoding='utf-8')
print(soup.prettify())
# print(soup.name)
print(soup.title.name)
# print(soup.p.attrs)
# # soup.p['class'] = 'myClass'  # 修改类名
# # print(soup.p)
# print(soup.p.string)
# print(type(soup.p.string))
# print(soup.head.contents)  # 返回列表
# print(len(soup.head.contents))
# print(soup.contents[1].string)
# print(soup.find_all('p',limit=2)) # 返回一个列表
# for tag in soup.find_all(re.compile("^b")):
#     print(tag.name)
# for a in soup.find_all(True):
#     print(a.name)
# print(soup.select("title")) # css选择器查找
# print(soup.select("html and title"))
# print(soup.select("html>title"))
