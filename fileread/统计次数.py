#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/8 12:12
 
'''
# 纯数字列表计重
mylist = [2, 2, 4, 4, 5, 25, 2, 8, 3, 2]
myset = set(mylist)
for item in myset:
    print("the %d has found %d" % (item, mylist.count(item)))

a={}
for i in mylist:
    if mylist.count(i)>1:
        a[i]=mylist.count(i)
print(a)
# 字典去重
from collections import Counter
a=Counter([1,2,2,2,2,3,3,3,4,4,4,4])
print(a)