#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/21 12:32
 
'''
import re
import requests
import urllib
import urllib3

home_url = 'http://bj.lianjia.com/'
auth_url = 'https://passport.lianjia.com/cas/login?service=http%3A%2F%2Fbj.lianjia.com%2F'
chengjiao_url = 'http://bj.lianjia.com/chengjiao/'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'passport.lianjia.com',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
}

req = requests.get(home_url, headers=headers)
result = open(req)
pattern = re.compile(r'JSESSIONID=(.*)')
jsessionid = pattern.findall(result.info().getheader('Set-Cookie').split(';')[0])[0]

print(jsessionid)
