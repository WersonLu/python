#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
@File    : mongo插数据.py
'''
import pymongo

con = pymongo.MongoClient(host="127.0.0.1", port=27017)
mydb = con.baidu
col = mydb.info
num = 0
for i in col.find():
    print(i)
    num += 1
print(num)
