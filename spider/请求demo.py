#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
@File    : 请求demo.py
'''
import json
import requests


# url = 'http://www.etf.com/etf-finder-funds-api//-aum/0/20/1'
#
# # page = requests.get(url).content
# # print(page)


def get_page():
    default_request_header = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        # 'Cookie': '__cfduid=d56e890c4e6010702e6a0bbd4062dd2371520821430; has_js=1; _ga=GA1.2.1010010579.1520821464; _gid=GA1.2.54063564.1520821464; Drupal.session_cache.etf_com_session_dbor_information_obj=%22eyJ1bmlxaWQiOiJldGZfY29tXzE1MjA4MjE0MzE1YWE1ZTRiNzAyNDhjMi44MTI3ODc0NSIsInVzZXJpcCI6IjYxLjE0NC42Ni4yNiwgMTYyLjE1OC4yNTUuMTgyIiwibWVkaXVtIjoiIiwiY2FtcGFpZ25fRVRGV2F0Y2giOiIiLCJjYW1wYWlnbl93ZWVrbHluZXdzbGV0dGVyIjoiIiwiY2FtcGFpZ25fZGFpbHluZXdzbGV0dGVyIjoiIn0%22; _pk_ses.3.5465=*; _pk_id.3.5465=9bcf1072cb6eaec4.1520821465.3.1520842516.1520840919.; _gat=1',
        'Host': 'www.etf.com',
        'Referer': 'http://www.etf.com/etfanalytics/etf-finder',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'X-NewRelic-ID': 'UgcAVlBUGwQFU1NWAAUD',
        'X-Requested-With': 'X-Requested-With'
    }

    url = 'http://www.etf.com/etf-finder-funds-api//-aum/20/20/1'
    page = requests.get(url, headers=default_request_header).content
    datas = json.loads(page)
    for data in datas:
        # print(data)
        ticker = data['ticker']
        exr = data['fundBasics']['expenseRatio']['value']
        print(ticker, exr)


# for i in range(0, 2180, 20):
#     print(i)
import re

pattern = '<a[^>]*([^<]*)<a>'
string1 = '<a>你好啊</a>'
matobj = re.search(pattern, string1)
print(matobj.groups())
