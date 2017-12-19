#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/19 12:54
 
'''
import random
# from scrapy.http import Request
#
# from scrapy.utils.url import canonicalize_url

class RandomUserAgent(object):

    def __init__(self,agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls,crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))#返回的是本类的实例cls ==RandomUserAgent

    def process_request(self,request,spider):
        request.headers.setdefault('User-Agent', random.choice(self.agents))
