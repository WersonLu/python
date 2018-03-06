#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/20 10:20
 
'''
# 随机生成优惠券
import random
import pymysql


# 随机取多少位的优惠码多少个
def get_code(m):
    list = []
    for x in range(65, 91):
        a = str(chr(x))  # 生成对应的ascii码对应的字符串
        list.append(a)

    for x in range(97, 123):
        a = str(chr(x))  # 生成对应的ascii码
        list.append(a)
    for x in range(10):
        list.append(str(x))

    s = ''

    for x in range(m):
        a = random.choice(list)
        s = s + a
    print(s)


for x in range(5):
    get_code(2)
