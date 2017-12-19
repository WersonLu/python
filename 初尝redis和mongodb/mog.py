#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/19 11:12
 
'''
import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client.papers

