#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2018/1/10 2:24
 
'''

a = (lambda x: (lambda y: x + y))
b = a(99)
print(b(3))
l = [1, 2, 3, 4]
print(l[0])
print(l[1:])
res = l[0]
for i in l[1:]:
    # print(i)
    res = res + i
    print(res)

# 三种方法取偶数

y = [x for x in range(10) if x % 2 == 0]
print(y)
y1 = list(filter((lambda x: x % 2 == 0), range(10)))
print(y1)

z = []
for x in range(10):
    if x % 2 == 0:
        z.append(x)
print(z)

# ab = 99


def selector():
    # print(ab)
    global x
    print(x)
    x = 88
selector()

selector()

