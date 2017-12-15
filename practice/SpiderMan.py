#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/7 15:52
 
'''

from practice.DataOutput import DataOutput
from practice.HtmlDownloader import HtmlDownloader
from practice.HtmlParser import HtmlParse
from practice.URLManager import UrlManager


class SpiderMan(object):

    def __init__(self):
        self.manage = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParse()
        self.output = DataOutput()

    def crawl(self, root_url):
        # 添加入口URL
        self.manager.add_new_url(root_url)
        # 判断url管理器中是否有新的url，同时判断抓取了多少个url
        while (self.manager.has_new_url() and self.manager.old_url_size() < 100):
            # 从URL管理器获取新的url
            try:
                new_url = self.manager.get_new_url()
                # HTML下载器下载网页
                html = self.downloader.download(new_url)
                # HTML解析器抽取网页数据
                new_urls, data = self.parser.parser(new_url, html)
                # 将抽取的url添加到URL管理器中
                self.manager.add_new_urls(new_urls)
                # 数据存储器存储文件
                self.output.store_data(data)
                print("已经抓取%s个链接" % self.manager.old_url_size())
            except Exception as e:
                print(e)  # 数据存储器将文件输出成指定格式
            self.output.output_html()


if __name__ == "__main__":
    spider_man = SpiderMan()
    spider_man.crawl("http://baike.baidu/view/10812319.html")
