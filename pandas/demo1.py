#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     demo1
   Author :       aaa
   date：          2017/12/19
-------------------------------------------------
"""
import pandas as pd

obj = pd.Series([1, 4, 6, 3])

print(obj)

print(obj.values)  # 输出[1 4 5 3]
a = obj.index
print(a)  # RangeIndex(start=0, stop=4, step=1)

obj2 = pd.Series([1, 5, 73, 56], index=['a', 'c', 'e', 't'])

print(obj2)

print(obj2.index)  # Index(['a', 'c', 'e', 't'], dtype='object')

print(obj2['e'])  # 与list，key取值类似

print(obj2[obj2 > 5])
print('a' in obj2)  # true

# 如果数据被放入字典，可以直接创建series
data = {
    'liu': '伟',
    'a': 2,
    'v': 4
}
# 如果只有一个字典,那series的索引就是字典的k值
obj3 = pd.Series(data)
print(obj3)

states = ['o', 'p', 'q']
# 此时索引找不到对应值输出NaN
obj4 = pd.Series(data, index=states)
print(obj4)

print(pd.isnull(obj4))
# 此时因为输出的nan是空值所以输出true
# o    True
# p    True
# q    True
# dtype: bool

print(obj3 + obj4)  # 数据对齐

obj.name = 'population'
obj.index.name = 'state'  # 赋值更改索引
print(obj)

#reindex 会根据新索引重排

