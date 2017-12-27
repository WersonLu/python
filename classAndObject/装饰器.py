#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/27 8:08
 
'''


def foo(fo):
    print("foo函数正运行")
    return fo


@foo
def foo2():
    print("foo2函数在运行")


if __name__ == '__main__':
    foo2()
# foo函数正运行
# foo2函数在运行
