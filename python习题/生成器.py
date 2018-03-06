#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2018/3/2 8:13
 
'''
import time

# mygenerator = (x * x for x in range(3))
# for i in mygenerator:
#     print(i)


def fact(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i


numbers = [2139079, 1214759, 1516637]
start = time()
for number in numbers:
    list(fact(number))
end = time()
print("%s" % (end - start))
