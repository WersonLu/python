#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/7 11:16
 
'''
import lxml

import requests
import re
import csv
import json
from bs4 import BeautifulSoup

user_agent = 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
headers = {'User-Agent': user_agent}
r = requests.get('http://seputu.com/', headers=headers).text

html = lxml.etree.HTML(r)

div_mulus = html.xpath('.//*[@class="mulu"]')

rows = []

for div_mulu in div_mulus:
    div_h2 = div_mulu.xpath(('./div[@class="mulu-title"]/center/h2/text()'))
    if len(div_h2) > 0:
        h2_title = div_h2[0]
        a_s = div_mulu.xpath('./div[@class="box"]/ul/li/a')
        for a in a_s:
            href = a.xpath('./@href')[0].encode('utf-8')  # 字节
            box_title = a.xpath('./@title')[0]  # 字符串
            # print(href)
            pattern = re.compile(r'\s*\[(.*)\]\s+(.*)')
            # 不能在类似字节的对象上使用字符串模式
            result = re.search(pattern, box_title)
            # match = pattern.search(box_title)
            if result != None:
                date = result.group(1).encode('utf-8')
                real_title = result.group(2).encode('utf-8')
            # print(data)
            content = (h2_title, real_title, href, date)
            header = ['title', 'real_title', 'href', 'data']
            rows.append(content)
            with open('盗墓笔记.csv', 'w') as f:
                f_csv = csv.writer(f, )
                f_csv.writerow(header)
                f_csv.writerow(rows)
            f.close()
