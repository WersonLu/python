#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/7 14:01
 
'''


class UrlManager(object):
    def __init__(self):
        self.new_urls = set()  # 未爬取URL集合
        self.old_urls = set()  # 已爬取URL集合

        # 下面判断是否有未爬取的url

    def has_new_url(self):
        # 返回的集合大小不为0就是有新的
        return self.new_url_size() != 0

        # 下面获取一个未爬取的url

    def get_new_url(self):
        # pop方法从集合中取一个值并返回这个值,把这个值赋给未爬取的new_url
        new_url = self.new_urls.pop()
        # 把取到的一个url放到未爬取集合中
        self.old_urls.add(new_url)
        # 返回这一个未爬取的url
        return new_url

    def add_new_url(self, url):
        if url is None:
            return

        # 如果取到的url既不在未爬取集合里面,已不再已爬取集合里面,把它放入未爬取集合
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):

        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def new_url_size(self):
        # 返回未爬取url集合大小
        return len(self.new_urls)

    def old_url_size(self):
        # 返回已爬取集合大小
        return len(self.old_urls)
