#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/16 16:34
 
'''
import re
from scrapy import Selector
import scrapy
from cnblogSpider.items import CnblogspiderItem


# 爬虫的下载器
class CnblogsSpider(scrapy.Spider):
    name = "cnblogs"
    allowed_domains = ["cnblogs.com"]
    start_urls = ["http://www.cnblogs.com/qiyeboy/default.html?page=1"]

    def parse(self, response):
        papers = response.xpath(".//*[class='day']")
        for paper in papers:
            # extract 返回list列表
            url = paper.xpath(".//*[@class='postTitle']/a/@href").extract()[0]
            title = paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0]
            time = paper.xpath(".//*[@class='dayTitle']/a/text()").extract()[0]
            content = paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0]
            # print(url, title, time, content)
            item = CnblogspiderItem(url=url, title=title, time=time, content=content)
            yield item
            next_page = Selector(response).re(u'<a href="(\S*)">下一页</a>')
            if next_page:
                yield scrapy.Request(url=next_page[0], callback=self.parse())
