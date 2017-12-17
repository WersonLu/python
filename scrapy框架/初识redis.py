#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     初识redis
   Author :       aaa
   date：          2017/12/13
-------------------------------------------------
"""
import redis

r = redis.Redis(host='127.0.0.1', port=6379)
r.set('name', 'qiye')
print(r.get('name'))
