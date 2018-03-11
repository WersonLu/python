#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
列表推导,元组再研究
'''
s = 'cdf'
# 局部作用域  不影响变量对象上下文引用
a = [ord(s) for s in 'avf']
print(a)
print(s)

sy = '$daf'
filter_sy = [ord(a) for a in sy if ord(a) > 50]
print(filter_sy)

filter_sy1 = list(filter(lambda b: b > 50, map(ord, sy)))
print(filter_sy1)

# 元组拆包,可以嵌套拆包
lax = (22, -19)
c, d = lax
print(c, d)

import os

# 在进行拆包的时候， 我们不总是对元组里所有的数据都感兴趣， _ 占位
# 符能帮助处理这种情况
_, filename = os.path.split('')
print(filename)

# *args 来获取不确定的参数    平行赋值
e, r, *test = range(5)
print(test)

"""
具名元组
用 namedtuple 构建的类的实例所消耗的内存跟元组是一样
的， 因为字段名都被存在对应的类里面。 这个实例跟普通的对象实
例比起来也要小一些， 因为 Python 不会用 __dict__ 来存放这些实
例的属性。

"""

# 切片赋值,删除,嫁接
l = list(range(10))
print(l[3::2])
l[2:4] = ["da", "de"]
print(l)

board = [['_'] * 3 for i in range(3)]
print(board)
board[1][2] = 'x'
print(board)

# 一个+=的问题
t = (1, 2, [30, 49])
t[2] += [33.56]
print(t)

"""
# list.sort 方法返回none,它会修改原来的列表 ,而sorted排序会新建一个列表
"""
