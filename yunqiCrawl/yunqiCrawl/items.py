# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# define the fields for your item here like:
# name = scrapy.Field()
# 基本信息
class YunqiBookListItem(scrapy.Item):
    novelId = scrapy.Field()
    novelName = scrapy.Field()
    novelLink = scrapy.Field()
    novelAuthor = scrapy.Field()
    novelType = scrapy.Field()
    novelStatus = scrapy.Field()
    novelUpdateTime = scrapy.Field()
    novelWords = scrapy.Field()
    novelImageUrl = scrapy.Field()


# 热度
class YunqiBookDetailItem(scrapy.Item):
    novelId = scrapy.Field()
    novelLabel = scrapy.Field()
    novelAllClick = scrapy.Field()
    novelMonthClick = scrapy.Field()
    novelWeekClick = scrapy.Field()
    novelAllPopular = scrapy.Field()
    novelMonthPopular = scrapy.Field()
    novelWeekPopular = scrapy.Field()
    novelCommentNum = scrapy.Field()
    novelAllComm = scrapy.Field()
    novelMonthComm = scrapy.Field()
    novelWeekComm = scrapy.Field()
