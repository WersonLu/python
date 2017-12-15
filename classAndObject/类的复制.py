#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/6 15:16
 
'''


class complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, "+", self.y, "i")


c1 = compile(1, 2)  # 有名对象
c2 = c1

print(id(c1), id(c2))
