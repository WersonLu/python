#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     jiupa
   Author :       aaa
   date：          2017/12/9
-------------------------------------------------
"""

import requests

import json

with open('jiupai.txt', "a")as f:
    for i in range(1, 20):
        url = 'http://appjph.jiupaicn.com/app/content/hot/list?type=1&page=' + str(i) + '&pageSize=10&_=1512821417704'
        webdata = requests.get(url).text

        data = json.loads(webdata)
        news = data['resultData']

        for n in news:
            title = n['title']
            name = n['memberName']
            f.write(title + name + '\n')
            print(title + name)

