#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
@File    : demo4.py
'''

# 函数 式编程

a = list(filter((lambda x: x > 0), range(-5, 5)))
print(a)

res = []
for x in range(-5, 5):
    if x > 0:
        res.append(x)
print(res)

from functools import reduce

b = reduce((lambda x, y: x + y), [1, 2, 3, 45])
print(b)

L = [1, 2, 3, 4]
res = L[0]
for x in L[1:]:
    res = res + x
print(res)

c = [x for x in range(5) if x % 2 == 0]
print(c)


def gensquare(N):
    for i in range(N):
        yield i ** 2


# d = gensquare(8)

D = {'a': 1, 'b': 2, 'c': 3}
x = iter(D)
print(next(x))

"""
计时脚本
"""
import timer

# 一般的,函数中没有赋值的变量名会在整个模块文件中查找
x = 99


def sel():
    print(x)
    # x=88  未定义的变量报错


sel()
"""
在函数参数前面加个*号,变成可变参数,在函数的内部接受的是一个tuple,函数不变,参数可以传任意个
 python允许你在list或者tuple前加一个*号,把list或tuple的元素变成可变参数传进去
关键字参数可以拓展函数的功能
"""


def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res


def lessthan(x, y): return x < y


print(minmax(lessthan, 4, 5, 6, 8, 9, 2))
