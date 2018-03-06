#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2018/3/5 19:20
 
'''
# 语法基础,文件,列表
print("中国**2")
a = '中国' * 2
print(a)

for x in '中国新时代':
    print(x)

import sys
import os

print(sys.platform)

# 遍历一层目录下的文件
g = [x for x in os.listdir('E:\python') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(len(g))
print(len.__doc__)

l = [1, 2, 3, 4]
l.append(l)
print(l)  # [1, 2, 3, 4, [...]]

import random

c = random.random()
print(c)

# 字符串不可变
gl = 'zhongguo'
print(gl[:])
print(gl[0:])
print(gl + 'xyz')
print(id(gl))
gl = 'a' + gl[1:]
print(id(gl))

# 序列化操作
L = [123, '1ad', 1.23]

L.append('ni')
print(L)
L.pop(2)  # 返回被去除的这个
print(L)

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [row[1] for row in m]
print(m2)

g = (sum(row) for row in m)
print(g)  # 生成器
print(next(g))

x = list(map(sum, m))
print(x)

# 字典
D = {'food': 'spam', 'quantity': 4, 'color': 'red'}
D['quantity'] += 1
print(D)

D1 = {'a': 1, 'b': 2, 'c': 3}
print(D1)
ks = list(D1.keys())
print(ks)
ks.sort()
for k in ks:
    print(k, '=>', D1[k])

x1 = 4
while x1 > 0:
    print('我' * x1)
    x1 -= 1

value = D1.get('x', 0)
print(value)
value = D1['x'] if 'x' in D1 else 5
print(value)

# 文件
f = open('data.txt', 'w')
f.write('hello\n')
print(f)

f.write('world\n')
f.close()
f2 = open('data.txt')
text = f2.read()
print(text)
print(text.split(','))  # 把文件切割成字符串(可选符合),

x = set('hello')
y = {'w', 'o', 'd', 'f', 'g'}
print(x, y)
print(x & y)  # 交集
print(x | y)  # 并集
print(x - y)

print(1 / 3)

y = set('avcdr')
print(y)

# 集合 add 方法  集合是无序的
# 列表 append 方法

# 对象引用
k1 = [2, 3, 4]
k2 = k1[:]  # 开辟新的地址
print(id(k1), id(k2))
k2[0] = 24
print(k1, k2)

A = ["span"]
B = A
B[0] = "span1"
print(A, B)
F = [1, 2, 3, 45]
print(id(F))
F[2] = 4
print(id(F), F)

# 基于字典的字符串格式化
s1 = "%(n)d %(x)s" % {"n": 1, "x": "spam"}
print(s1)
