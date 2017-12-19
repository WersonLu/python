#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     字符问题
   Author :       aaa
   date：          2017/12/19
-------------------------------------------------
"""
for i in range(1, 10):
    # print(i, '\n')  # '\n'自带回车功能,再加就空两行

    print(i, end='')  # 此时如加end,就取消了回车功能
    print(''.join(i))
