#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/7 11:11
 
'''
import csv

headers = ['id', 'username', 'password', 'age', 'country']
rows = [
    (1001, "qiye", 'wer', 23, 'china'),
    (1002, "qiye1", 'wer2', 23, 'china'),
    (1003, "qiye2", 'wer3', 23, 'china')
]
with open("qiye.csv", 'w')as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerow(rows)
f.close()
