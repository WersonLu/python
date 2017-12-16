#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/16 13:52
 
'''
import urllib.request
import requests


def download(blocknum, blocksize, totalsize):
    per = 100.0 * blocknum * blocksize / totalsize
    if per > 100:
        per = 100
        print("下载进度为%s" % per)


response = requests.get('https://api.jfbapp.cn/facemesh/billboard')

arr = response.json()['faces']
for i in arr:
    des = i['description']
    soce = i['score']
    url = i['image']
    try:
        urllib.request.urlretrieve(url, 'E:\\python\\爬虫\\图片\\' + des + '得分' + soce + '.jpg')
    except:
        continue
