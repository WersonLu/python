#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
@File    : 数组.py
'''

from array import array

from random import random

floats = array('d', (random() for i in range(10 ** 7)))
print(floats[-1])

fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10 ** 7)
fp.close()
print(floats2[-1])

"""
我们需要一个只包含数字的列表， 那么 array.array 比 list 更
高效。 数组支持所有跟可变序列有关的操作， 包括 .pop、 .insert 和
.extend。 另外， 数组还提供从文件读取和存入文件的更快的方法， 如
.frombytes 和 .tofile。

pickle.dump 处理各种类型也很快
"""

import numpy
a=numpy.arange(12)
print(a)
