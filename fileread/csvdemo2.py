#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2018/1/5 2:28
 
'''

import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsobj = BeautifulSoup(html)
# 找到表格中的第一个表
table = bsobj.find_all("table", {"class": "wikitable"})[0]
# 表中的所有行
rows = table.find_all("tr")
csvfile = open("wiki.csv", 'wt', newline="", encoding='utf-8')
writer = csv.writer(csvfile)
try:
    # 在这些行中循环取每一行
    for row in rows:
        scvRow = []
        for cell in row.find_all(['td', 'th']):
            scvRow.append(cell.get_text())
            writer.writerow(scvRow)
finally:
    csvfile.close()
