#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/19 17:05
 
'''

import sqlite3


class MobilePhone:

    def __init__(self):
        self.name = ''
        self.band = ''  # 品牌
        self.zolPhoneId = ''
        self.picUrl = ''  # 图片链接
        self.review = {...}
        self.price = {'平均售价': 0.0, '最高售价': 0.0, '最低售价': 0.0}
        self.attribute = {}
        self.attribute['基本参数'] = {...}
        self.attribute['屏幕'] = {...}
        self.attribute['网络'] = {...}
        self.attribute['外观'] = {...}
        self.attribute['硬件'] = {...}
        self.attribute['摄像头'] = {...}
        self.attribute['服务与支持'] = {...}
        self.attribute['手机附件'] = {'包装清单': '', '其他信息': ''}
        self.attribute['保修信息'] = {'保修政策': '', '质保时间': '', '质保备注': '', '客服电话': '',
                                  '电话备注': '', '详细内容': '', '其他信息': ''}


class DataBase:
    dbName = ''
    cursor = ''
    connet = ''

    numOfPhones = 0

    def __init__(self): ...

    def createTables(self): ...

    def save(self): ...

    def analyzeData(self): ...
