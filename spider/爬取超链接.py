#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/14 14:50
 
'''
import re
import urllib.request

# 提取超链接时,遇双引号会终止
# (http://\S*?)[\"] 提取不带" 符合的
# http://\S*?[\"] 提取带" 符合的
httpregex = re.compile(r"(http://\S*?)[\"]", re.IGNORECASE)

for line in urllib.request.urlopen("http://bbs.tianya.cn/m/post-140-393974-6.shtml"):
    line = line.decode("utf-8")

    mylist = httpregex.findall(line)
    if mylist:
        print(mylist)
