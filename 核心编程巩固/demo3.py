#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
@File    : demo3.py
'''


#  函数
def fu(a, *pargs):
    print(a, pargs)


print(fu(1, 1, 3))


# 1 (1, 3)
# None

def fu2(a, **kwargs):
    print(a, kwargs)


print(fu2(a=1, c=3, b=4))


# 1 {'c': 3, 'b': 4}
# None

# 递归函数
def mysum(L):
    print(L)
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])


a = mysum([2, 35, 67, 8])
print(a)


# 循环求和
def mysum1(L):
    sum = 0
    while L:
        print(L)
        sum += L[0]
        L = L[1:]
    return sum


b = mysum1([1, 2, 5, 57, 7])
print(b)

# for


