#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
@File    : pandas_csv.py
'''
import re
import pandas as pd
import csv

# df=pd.read_csv
# scv = ('QQmail.csv', encoding='utf-8', usecols=[2])

# friend = []
# for indexs in scv.index:
#     friend.append(scv.loc[indexs].values)
# friends = []
# for f in friend:
#     f = str(f).strip("[]'")
#     if re.search('@qq.com', f):
#         f = f[:-7]
#         friends.append(f)
# print(friends)
scv = csv.reader(open('QQmail5.csv', encoding='gbk'))
friends = []
for row in scv:
    friends.append(row[1])
print(friends)
