#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/13 16:40
 
'''


class 爷:
    def __init__(self):
        print("我创立了")


class 儿子(爷):
    def __init__(self):
        super().__init__()
        print("儿子构造了")


class 儿子1(爷):
    def __init__(self):
        super().__init__()
        print("幺儿子构造了")


class 媳妇(爷, 儿子, 儿子1):
    def __init__(self):
        # 儿子.__init__(self)
        # 儿子1.__init__(self)
        # 爷.__init__(self)
        super().__init__()


xf = 媳妇()  # 此时父类会多次构造浪费内存
