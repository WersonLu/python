#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: 字符串.py
 
@time: 2017/12/4 14:37
 
@desc:
 
'''
# mys = "heloworld"
# print(mys[3])
# print(mys[3:-1])  # 从前面开始，不包括后面
#
# mlist = [1, 2, 3, 4, 5, 6, 7]
# mlist.remove(1)
# print(mlist)
# print(mlist[4:-1])
# print(mlist[:])
# print(mlist[:4])
# print(mlist[4:])
# print(mlist * 2)  # 叠加[1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7]
#
# mtuple = (1, 2, 3, 4, 5, 6, 7)
# print(mtuple[:])
# print(mtuple[4:])
# print(mtuple[:4])
# print([x * x for x in range(10) if x % 2 == 1])  # 列表构造表达式
#
# print([x % 2 == 0 for x in range(100)])
#
# print(repr(1 + 2 + 3))
#
# print(int("16", 8))  # 进制转换
# print(hex(100))
# print(oct(10))
# 去重
list1 = [3, 2, 1, 4, 5, 6, 5, 4, 3, 2, 1]
print(list1, type(list1))
list1 = set(list1)
print(list1, type(list1))

list2 = set([4, 5, 6, 7, 8, 9])
print(list2)
# 交集
print(list1.intersection(list2))

# 并集
print(list1.union(list2))

# 差集
print(list1.difference(list2))
print(list2.difference(list1))

# 子集、父集
print(list1.issubset(list2))
print(list1.issuperset(list2))

list3 = set([4, 5, 6])
print(list3.issubset(list2))
print(list2.issuperset(list3))

# 对称差集
print(list1.symmetric_difference(list2))

# Return True if two sets have a null intersection
list4 = set([1, 2, 3])
print(list3.isdisjoint(list4))
# 交集
print(list1 & list2)
# union
print(list2 | list1)
# difference
print(list1 - list2)
# 对称差集
print(list1 ^ list2)
# 添加
list1.add(999)  # 添加一项
print(list1)
list1.update([66, 77, 88])  # 添加多项
print(list1)
print(list1.add(999))  # 猜猜打印什么？为什么

# 删除
list1.remove(999)
print(list1)

# remove and return arbitrary set element
print(list1.pop())

# Remove an element from a set if it is a member.If the element is not a member, do nothing.
print(list1.discard(888))
