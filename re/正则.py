#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/13 18:05
 
'''
import re

my = "<title>百度一下</title>"

line="a,c b;d"
mystr=re.split(r"[\s\,\;]",line)
print(mystr)