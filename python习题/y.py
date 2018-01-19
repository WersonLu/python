# !/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2018/1/8 10:17
 
'''
x = 10
while x:
    x = x - 1
    if x % 2 != 0: continue
    print(x, end=' ')

sum = 0
for i in [1, 2, 3, 4, 5]:
    sum = sum + i
print(sum)
