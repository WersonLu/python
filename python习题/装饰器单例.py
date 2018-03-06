#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2018/3/1 22:27
 
'''


# 闭包装饰器单例
def singl(cls, *args, **kwargs):
    isinstance = {}

    def getinstance():
        if cls not in isinstance:
            isinstance[cls] = cls(*args, **kwargs)
        return isinstance[cls]

    return getinstance


@singl
class myClass:
    pass
