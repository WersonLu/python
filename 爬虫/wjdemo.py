#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2018/1/4 4:56
 
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

# html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
# bsobj = BeautifulSoup(html)
# for link in bsobj.find_all("a"):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])
html = requests.get("https://www.hao123.com").content
bsobj = BeautifulSoup(html, "lxml")
for link in bsobj.find_all("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])
