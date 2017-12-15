#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: daikuan.py
 
@time: 2017/12/2 13:50
 
@desc:
 
'''
# 贷款计算器

year = eval(input("请输入贷款年限"))
money = eval(input("贷款金额"))
monthate = eval(input("请输入月利率"))

monthmoney = (money * monthate) / (1 - 1 / (1 + monthate) ** (year * 12))
allmoey = monthmoney * 12 * year
print("月供", monthmoney)
print("全部", allmoey)
