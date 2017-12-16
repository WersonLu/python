#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/16 13:28
 
'''
import urllib
import urllib.request
from lxml import etree
import requests


def download(blocknum, blocksize, totalsize):
    per = 100.0 * blocknum * blocksize / totalsize
    if per > 100:
        per = 100
        print("下载进度为%s" % per)


user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

headers = {'User-Agent': user_agent}
r = requests.get('http://www.ivsky.com/tupian/ziranfengguang/', headers=headers)
html = etree.HTML(r.text)

img_urls = html.xpath('.//img/@src')
i = 0
for img_url in img_urls:
    # 下载路径 存放路径
    urllib.request.urlretrieve(img_url, 'E:\python\爬虫\图片\img' + str(i) + '.jpg', download)
    i += 1
