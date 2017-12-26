#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/26 16:02
 
'''
import re
import requests
from requests.exceptions import RequestException


def get_one_page(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=header)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    pass


# 解析


def main():
    url = 'http://maoyan.com/board/4?'
    html = get_one_page(url)
    print(html)


if __name__ == '__main__':
    main()
