#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2018/1/20 9:58
 
'''
import pandas as pd

# ,chunksize=2000,low_memory=False
df = pd.read_csv('E:\\2000W\\800W-1000W.csv', iterator=True)

# print(df.shape)  # (2000053, 33) 200万条,33行
# print(df.describe())
chuck = df.get_chunk(5).head()
print(chuck)
