#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/7 12:48
 
'''

import urllib
import lxml
import requests


def Schedule(blockm, blocksize, totalsize):
    per = 100.0 * blockm * blocksize / totalsize
    if per > 100:
        per = 100
        print('当前进度:%s' % per)


user_agent = 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
headers = {'User_Agent': user_agent}
r = requests.get('http://www.ivsky.com/tupian/ziranfengguang/', headers=headers).text

html = lxml.etree.HTML(r)
img_urls = html.xpath('.//img/@SRC')
i = 0
for img_url in img_urls:
    urllib.urlretrieve(img_url, 'img' + str(i) + '.jpg', Schedule())
    i += 1
