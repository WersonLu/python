# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import pymongo
from yunqiCrawl.items import YunqiBookDetailItem, YunqiBookListItem


class YunqicrawlPipeline(object):

    def __init__(self, mongo_uri, mongo_db, replicaset):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.replicaset = replicaset

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.setting.get('MONGO_URI'),
            mongo_db=crawler.setting.get('MONGO_DB'),
            replicaset=crawler.setting.get('REPLICASET')

        )

    # 打开爬虫初始化数据库连接
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri, replicaset=self.replicaset)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if isinstance(item, YunqiBookListItem):
            self._process_booklist_item(item)
        else:
            self._process_bookDetail_item(item)
        return item

    def _process_booklist_item(self, item):
        self.db.bookinfo.insert(dict(item))

    def _process_bookeDetail_item(self, item):
        pattern = re.compile('\d+')
        item['novelLabel'] = item['novelLabel'].strip().replace('\n', '')

        match = pattern.search(item['novelAllClick'])
        item['novelAllClick'] = match.group() if match else item['novelAllClick']

        match = pattern.search(item['novelMonthClick'])
        item['novelMonthClick'] = match.group() if match else item['novelMonthClick']

        match = pattern.search(item['novelWeekClick'])
        item['novelWeekClick'] = match.group() if match else item['novelWeekClick']

        match = pattern.search(item['novelAllPopular'])
        item['novelAllPopular'] = match.group() if match else item['novelAllPopular']

        match = pattern.search(item['novelMonthPopular'])
        item['novelMonthPopular'] = match.group() if match else item['novelMonthPopular']

        match = pattern.search(item['novelWeekPopular'])
        item['novelWeekPopular'] = match.group() if match else item['novelWeekPopular']

        match = pattern.search(item['novelAllComm'])
        item['novelAllComm'] = match.group() if match else item['novelAllComm']

        match = pattern.search(item['novelMonthComm'])
        item['novelMonthComm'] = match.group() if match else item['novelMonthComm']

        match = pattern.search(item['novelWeekComm'])
        item['novelWeekComm'] = match.group() if match else item['novelWeekComm']

        self.db.bookhot.insert(dict(item))
