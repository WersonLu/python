#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/14 14:18
 
'''
# 爬取邮箱
import urllib
import urllib.request  # 请求
import re

mailregex = re.compile(r"([A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4})", re.IGNORECASE)
qqregex = re.compile(r"[1-9]\d{4,10}", re.IGNORECASE)
'''
for  line  in urllib.request.urlopen("http://bbs.tianya.cn/m/post-140-393974-6.shtml"):
    mylist=mailregex.findall(line.decode("utf-8"))
    if  mylist:
        print(mylist)
'''
mystr = urllib.request.urlopen("http://bbs.tianya.cn/m/post-140-393974-6.shtml").read()
mylist = mailregex.findall(mystr.decode("utf-8"))
print(mylist)
# f = open("邮箱.txt", "wb")
# f.write(mylist)

# f.close()


