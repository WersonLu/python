#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     dataframedemo
   Author :       aaa
   date：          2017/12/19
-------------------------------------------------
"""
import pandas as pd
import numpy as np

data = {
    'state': ['ohio', 'ohio', 'ohio', 'nevada', 'new'],
    'year': [2000, 2001, 2004, 2003, 2002],
    'pop': [1.5, 1.7, 8, 2.5, 5]
}
frame = pd.DataFrame(data)

print(frame)  # 加上索引有序排列

frame1 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'])  # 更改字段顺序
print(frame1)  # 找不到则为nan
#    year   state  pop debt
# 0  2000    ohio  1.5  NaN
# 1  2001    ohio  1.7  NaN
# 2  2004    ohio  8.0  NaN
# 3  2003  nevada  2.5  NaN
# 4  2002     new  5.0  NaN
print(frame1['state'])  # 通过字典标记的方式,将其一列获取成一个series

frame1['debt'] = 18  # 赋一个标量值或者一组值
print(frame1)

frame1['debt'] = np.arange(5.)  # 赋值浮点
print(frame1)

val = pd.Series(['a', 'c', 'e', 't'], index=[1, 5, 73, 56])
frame1['debt'] = val
print(frame1)  # 索引匹配则赋值.不匹配则赋值NaN

# 嵌套字典 外层字典的键作为列,内层健作为行索引

pop = {'nevada':
           {2001: 2.4,
            2002: 4},
       'abb': {
           2000: 1.5, 2001: 3.5, 2004: 8
       }
       }
print(pd.DataFrame(pop))  # 同样可以显示的指定索引
