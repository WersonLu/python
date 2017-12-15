#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/9 13:33
 
'''


class namemoney:
    def __init__(self, name, money):  # self 自身

        print("hello python")
        self.name = name
        self.money = money

    def cunkuan(self, num):
        print(self.name, '存款', num)
        self.money += num

    def qukuan(self, num):
        print(self.name, "取款", num)
        self.money -= num



werson = namemoney("刘伟",10000)  # 调用函数

print(werson.name)
print(werson.money )
print(werson.cunkuan(100))