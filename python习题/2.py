#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2018/1/27 13:30
 
'''
l = ['abc', 'ABD', 'aBe']
l1 = sorted(l, key=str.lower, reverse=True)
print(l1)
# 转为小写排序
l2 = sorted([x.lower() for x in l], reverse=True)
print(l2)

# l[1:] = []
# print(l)
del l[1:]
print(l)

D = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
print(D)
D1 = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
print(D1)

D2 = dict.fromkeys(['a', 'b', 'c'], 1)
print(D2)

D3 = {k: 0 for k in ['a', 'b', 'c']}
print(D3)

D4 = dict(a=1, b=2, c=3)
print(D4)

# 创建列表
G = []
i = 0
while i < 5:
    G.append(0)
    i += 1
print(G)

G1 = ([0 for i in range(5)])
print(G1)



