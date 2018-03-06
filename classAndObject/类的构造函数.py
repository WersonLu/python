#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/9 15:54
 
'''


class namemoney:
    def __init__(self):  # 初始化时调用
        print("构造了", id(self))

    def __del__(self):  # 删除时调用
        print("删除了")


zhangs = namemoney()
print(zhangs)
