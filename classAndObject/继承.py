#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/11 14:09
 
'''


class 王健林:
    def __init__(self):
        self.name = "王健林"
        self.mystr = "先定一个小目标，赚它一个一亿"
        self.money = 200000000000

    def show(self):
        print("我是", self.name, '我有', self.money)


class 王思聪(王健林):  # 继承，
    def __init__(self):
        super().__init__()  # 调用王健林打下的根基     super()父类，初始化，
        self.name = "王思聪"


wjl = 王健林()
wjl.show()
# 继承方法属性,自由属性覆盖父类同名属性
wsc = 王思聪()
wsc.show()
