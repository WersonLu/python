#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     进程共享字典list
   Author :       aaa
   date：          2017/12/15
-------------------------------------------------
"""
import multiprocessing


def fun(mydict, mylist):
    mydict["key1"] = "搞基大队"
    mydict["key2"] = "爆菊大队"
    mylist.append(1)
    mylist.append(2)
    mylist.append(3)
