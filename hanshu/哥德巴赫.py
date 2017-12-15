#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: 哥德巴赫.py
 
@time: 2017/12/4 12:41
 
@desc:
 
'''
import math
import time
from multiprocessing import cpu_count
from multiprocessing import Pool


# 判断质数
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


print(id(isPrime))
print(type(isPrime)) #函数的类型
print(type(isPrime(2))) #返回值的类型
