#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/7 14:39
 
'''
import requests

# html下载器
class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        user_agent = 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
        headers = {'User_Agent': user_agent}

        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            r.encoding = 'utf-8'
            return r.text
        return None
