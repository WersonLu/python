#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
@File    : demo2.py
'''


# 语句
def ji_suan():
    while True:
        reply = input('enter text:')
        if reply == 'stop':
            break
        print(int(reply) ** 3)
    print('再见')


# try处理
def jssuan():
    while True:
        reply = input('输入')
        if reply == 'stop':
            break
        try:
            num = int(reply)
        except:
            print('bad')
        else:
            print(num ** 2)
    print('再见')


# jssuan()

dic = {'a': 31, 'bc': 5, 'c': 3, 'asd': 4, 'aa': 74, 'd': 0}
dict1 = sorted(dic.items(), key=lambda d: d[1], reverse=True)
print(dict1)

# 修改列表
L = [1, 2, 3, 4, 5]
for i in range(len(L)):
    L[i] += 1
print(L)
a1=[X + 1 for X in L]
print(a1)


