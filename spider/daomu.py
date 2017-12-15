#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/7 9:47
 
'''

import requests
import json
from bs4 import BeautifulSoup

user_agent = 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
headers = {'User-Agent': user_agent}
r = requests.get('http://seputu.com/', headers=headers).text
# print(r)
soup = BeautifulSoup(r, 'html.parser', from_encoding='utf-8')

# 把文件写入文本文件
# with open('盗墓笔记.txt', 'a+', encoding='utf-8') as f:
#     for mulu in soup.find_all(class_="mulu"):  # 找到类名为目录下的所有内容
#         h2 = mulu.find('h2')  # 在目录里的大标题
#         if h2 != None:
#             h2_title = h2.string
#             # 目录的子元素box，在box中找到所有a标签
#             for a in mulu.find(class_='box').find_all('a'):
#                 # 在a标签中取得href，和标题
#                 href = a.get('href')
#                 box_title = a.get('title')
#                 # 写入文件自动换行
#                 f.write(href + "" + box_title + '\n')
#                 print(href, box_title)
# f.close()
# 把文件写入json
content = []
for mulu in soup.find_all(class_="mulu"):
    h2 = mulu.find('h2')
    if h2 != None:
        h2_title = h2.string
        # 定义一个列表
        list = []
        for a in mulu.find(class_='box').find_all('a'):
            href = a.get('href')
            box_title = a.get('title')

            list.append({'href': href, 'box_title': box_title})
            content.append({'h2': h2_title, 'content': list})
            with open('盗墓笔记.json', 'wb')as f:
                json.dump(content, fb=f, indent=4)
            fp.close()
