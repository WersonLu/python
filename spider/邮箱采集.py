#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
@File    : 邮箱采集.py
'''

import requests, re

# regex = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
# 这个正则表达式过滤掉了qq邮箱
regex = r"([a-zA-Z0-9_.+-]+@[a-pr-zA-PRZ0-9-]+\.[a-zA-Z0-9-.]+)"
# 基于隐私，使用了“XXXXXXXXXXXXXX”
url = 'https://perfil.mercadolivre.com.br/LAGOS+DIGITAL'
html = requests.get(url).text
# print(html)
emails = re.findall(regex, html)
i = 0
for email in emails:
    i += 1
    if i < 16:
        print("{} :{}".format(i, email))
