#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2018/1/6 2:56
 
'''
import requests

files = {'uploadFile': open("1.txt", 'rb')}
r = requests.post(url="", files=files)
print(r.text)
