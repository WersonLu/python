#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/15 10:10
 
'''
import urllib
import urllib.request
import re


def getpage(path):
    data = urllib.request.urlopen(path).read().decode("gbk")  # 中文网页
    return data


# find没有括号抓取全部，有括号，抓取括号内，内容有括号转义字符 \( \)

def getcode(data):
    # regex_str="<li><a target=\"_blank\" href=\"http://quote.eastmoney.com/(\S\S.*?).html\">"
    regex_str = " <li><a target=\"_blank\" href=\"http://quote.eastmoney.com/(\S\S.*?).html\">(.*?)\("
    pat = re.compile(regex_str)  # 预编译
    codelist = pat.findall(data)
    return codelist


path = "http://quote.eastmoney.com/stocklist.html"
data = getpage(path)  # 抓取了网页源代码
codelist = getcode(data)
# print(codelist)

for code in codelist:
    print(code[0], code[1])
