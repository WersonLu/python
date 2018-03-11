#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
@File    : 字典集合.py
'''

# 字典构造法
import collections

a = dict(one=1, two=2, three=3)
print(a)

b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip([], []))
d = dict({'one': 1, 'two': 2, 'three': 3})

e = dict([('two', 2), ('one', 1), ('three', 3)])

# 自定义映射类
"""
isinstance() 函数用来判断一个对象是否是一个已知的类型,类似type()
    type 不考虑继承关系  isinstance()会考虑

"""


class StrKeyDict0(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d['2'])
print(2 in d)

"""
字典的变种
"""

# 统计各字母的次数
ct = collections.Counter('aaaddddeec')
print(ct)


class StrKryDict(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    # 把所有的键都转换成字符串
    def __setitem__(self, key, item):
        self.data[str(key)] = item

#
# d1 = StrKryDict('1', '刘伟')
# print(d1.__setitem__())

# 一个测试

# found=0
# for n in needles:
#     if n
