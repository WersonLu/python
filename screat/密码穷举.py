#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/9 11:39
 
'''
import itertools

mylist = list(itertools.permutations([1, 2, 3, 4], 4))  # 可以无序
print(mylist)

mylist2 = list(itertools.combinations([1, 2, 3, 4], 4))  # 一定有序
print(mylist2)

# 重复密码
mylist3 = (["".join(x) for x in itertools.product("12345abcdexf", repeat=4)])
print(len(mylist3))
print(mylist3)

file=open("bank.txt","wb")
for i in mylist3:
    file.write((i+"\r\n").encode('utf-8'))

file.close()

# 这()是一个generator生成器
mylist4=["".join(x)for x in itertools.product("012345abcdef",repeat=4)]
print(type(mylist4))
