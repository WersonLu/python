#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     台阶问题
   Author :       aaa
   date：          2017/12/14
-------------------------------------------------
"""


# 树状递归，指数级增长
def go(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        return go(num - 1) + go(num - 2)


print(go(15))
