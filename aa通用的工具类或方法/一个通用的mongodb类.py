#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
@File    : 一个通用的mongodb类.py
'''

from pymongo import MongoClient

"""
在爬虫存数据时使用,不需要事先建立数据库,直接存字典
"""


class MyMongo:

    def __init__(self, dbname, colname):
        """

        :param dbname: 初始化 命名自己的库
        :param colname: 初始化 命名自己的表(集合)名
        """
        # host,port 按自己需要重写
        self.host = "127.0.0.1"
        self.port = 27017
        # self.dbname = dbname
        # self.colname = colname
        self.client = MongoClient(host=self.host, port=self.port)
        self.db = self.client[dbname]
        self.col = self.db[colname]

    def process_data(self, data):
        self.col.insert(data)
        print("成功插入%s" % data)

    def close_mongo(self):
        self.client.close()
    # 其他增删改查操作


my = MyMongo("wnagyi", "info")
my.process_data({"姓名": "刘伟", "工资": 1800})
my.close_mongo()
