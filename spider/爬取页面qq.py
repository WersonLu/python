#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/14 14:47
 
'''
import urllib.request  # 请求
import re

QQregex = re.compile(r"[1-9]\d{4,10}", re.IGNORECASE)

for line in urllib.request.urlopen("http://bbs.tianya.cn/m/post-140-393974-6.shtml"):
    line = line.decode("utf-8")
    if line.find("QQ") != -1 or line.find("Qq") != -1 or line.find("qq") != -1:
        mylist = QQregex.findall(line)
        if mylist:
            print(mylist)
