#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/6 15:13
 
'''


class complex_a:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, "+", self.y)


# 实例化有名对象
c1 = complex_a(1, 4)
c1.show()
# 实例化匿名对象
complex_a(1, 6).show()
