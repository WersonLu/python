#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2018/1/6 3:36
 
'''
#  WebDriverWait 和 expected_conditions，
# 这两个模块组合起来构成了 Selenium 的隐式等待（ implicit wait）。
import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('user', 'password')
r = requests.post(url="", auth=auth)
print(r.text)
