#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/14 16:22
 
'''
# 挖掘任意页面邮箱
import urllib.request
import urllib
import re


# httpregex = re.compile(r"(http://\S*?)[\"|>|]", re.IGNORECASE)
#
# for line in urllib.request.urlopen("http://bbs.tianya.cn/m/post-140-393974-6.shtml"):
#     line = line.decode("utf-8")
#
#     mylist = httpregex.findall(line)
#     if mylist:
#         print(mylist)

def getdata(url):
    try:
        data = urllib.request.urlopen(url).read().decode('utf-8')
        return data
    except:
        return ""
    return


def getallemail(data):
    try:
        mailregex = re.compile(r"([A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4})", re.IGNORECASE)
        mylist = mailregex.findall(data)
        return mylist
    except:
        return []


print(getallemail(getdata("http://bbs.tianya.cn/m/post-140-393974-6.shtml")))
