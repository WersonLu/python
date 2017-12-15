#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     json转换
   Author :       aaa
   date：          2017/12/9
-------------------------------------------------
"""
import json

data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'

}
json_str = json.dumps(data) # json对象


print(repr(data))  # python原始数据
print(json_str)  # 多个双引号有何区别
json1 = json.loads(json_str)  #json 对象转为字典
print(json1)
