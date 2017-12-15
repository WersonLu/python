#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: zhilian.py
 
@time: 2017/12/5 15:11
 
@desc:
 
'''
# import requests
# from bs4 import BeautifulSoup
# import re
#
# url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=全国&kw=python&p=1&kt=3'
# wbdata = requests.get(url).content
# soup = BeautifulSoup(wbdata, 'lxml')
#
# items = soup.select("div#newlist_list_content_table > table")
# count = len(items) - 1
# print(count)
#
# job_count = re.findall(r"共<em>(.*?)</em>个职位满足条件", str(soup))[0]
# pages = (int(job_count) // count) + 1
# print(pages)
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool


def get_zhaopin(page):
    url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?jl=全国&kw=python&sm=0&p={}'.format(page)
    print("第{0}".format(page))
    wbdata = requests.get(url).content
    soup = BeautifulSoup(wbdata, 'lxml')

    job_name = soup.select("table.newlist>tr>td.zwmc>div>a")
    salarys = soup.select("table.newlist > tr > td.zwyx")
    locations = soup.select("table.newlist > tr > td.gzdd")
    times = soup.select("table.newlist > tr > td.gxsj > span")

    for name, salary, location, time in zip(job_name, salarys, locations, times):
        data = {
            'name': name.get_text(),
            'salary': salary.get_text(),
            'location': location.get_text(),
            'time': time.get_text(),
        }
        print(data)  # 是


if __name__ == '__main__':
    pool = Pool(processes=2)
    pool.map_async(get_zhaopin, range(1, 10 + 1))
    pool.close()
    pool.join()
