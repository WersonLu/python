#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/23 5:58
 
'''
import pandas as pd
import numpy as np
# from numpy import *
# from pandas import *
import matplotlib.pyplot as plt

# ts = pd.Series(random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
# ts = ts.cumsum()
# ts.plot()
# plt.show()

# s = pd.Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
# s.plot()  # series dataframe 都有plot方法画图
# plt.show()

df = pd.DataFrame(np.random.randn(10, 4).cumsum(),
                  columns=['a', 'b', 'c', 'd'],
                  index=np.arange(0, 100, 10))
df.plot()  # plot方法有很多参数,水平柱状图,颜色,透明度等

plt.show()

