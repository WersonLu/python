#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     爬取淘宝mm基本信息
   Author :       aaa
   date：          2017/12/17
-------------------------------------------------
"""
# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-12-17 16:29:00
# Project: tbmm

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    def __init__(self):
        self.base_url = 'https://mm.taobao.com/json/request_top_list.htm?page='
        self.page_num = 1
        self.total_num = 30

    @every(minutes=24 * 60)
    def on_start(self):
        while self.page_num <= self.total_num:
            url = self.base_url + str(self.page_num)
            print(url)
            self.crawl(url, callback=self.index_page)
            self.page_num += 1

    @config(age=10 * 24 * 60 * 60)
    # 此时response就是单个网页的内容,doc是pyquery函数
    def index_page(self, response):
        for each in response.doc('.lady-name').items():
            self.crawl(each.attr.href, callback=self.detail_page, fetch_type='js')

    # 最后的详情页,可以取这页的基本资料,也可以取最终个性域名的图片
    @config(priority=2)
    def detail_page(self, response):
        return {
            "name": response.doc('.mm-p-base-info>.mm-p-info-cell>li:nth-child(1)>span').text(),
            "url": 'https:' + response.doc(' div.mm-p-info.mm-p-domain-info > ul > li > span').text(),
            "school": response.doc('.mm-p-info-cell>li:nth-child(6)>span').text(),
            "city": response.doc('.mm-p-info-cell>li:nth-child(3)>span').text(),
            "fans": response.doc('.mm-p-info-fans>dt>a').text()
        }

    def domain_page(self, response):
        pass
