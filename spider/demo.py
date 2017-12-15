#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: demo.py
 
@time: 2017/12/6 9:54
 
@desc:
 
'''
import requests
import urllib.request

with urllib.request.urlopen('http://www.python.org/') as f:
    print(f.read(),end="")

