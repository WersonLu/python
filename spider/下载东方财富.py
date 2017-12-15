#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/15 13:42
 
'''
import urllib
import urllib.request
import re

# 下载路径
# url = ""
# # 存放路径
# path = "E:\\数据文件\\股票下载\\1.jpg "
# urllib.request.urlretrieve(urllib, path)

# 神秘接口
url = "http://quotes.money.163.com/service/chddata.html?code=100700&end=20130523&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
path = "E:\\数据文件\\股票下载\\00700.csv"
urllib.request.urlretrieve(url, path)
