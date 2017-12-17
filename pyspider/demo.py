#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     demo
   Author :       aaa
   date：          2017/12/17
-------------------------------------------------
"""
from pyquery import PyQuery as pq

# pq可以读取属性样式也可以修改
d = pq('<p id="hello" class="world",></p>')
print(d.attr("id"))
