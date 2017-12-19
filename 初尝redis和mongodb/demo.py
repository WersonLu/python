#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     demo
   Author :       aaa
   date：          2017/12/18
-------------------------------------------------
"""
import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)
r.set('name', 'liuwei')
print(r.get('name'))
