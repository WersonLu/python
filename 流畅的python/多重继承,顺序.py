#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
@File    : 多重继承,顺序.py
'''


class A:
    def ping(self):
        print('屏', self)


class B(A):
    def pong(self):
        print('平', self)


class C(A):
    def pong(self):
        print('平1', self)


class D(C, B):
    def ping(self):
        super.ping()
        print('post-ping', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)


"""
类有一个__mro__属性,值是一个元组,解析各个超类,直到object
用super可把方法委托给超类

super() 函数是用于调用父类(超类)的一个方法。
super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。
MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表
"""

d = D()
print(d.pong())
# print(d.ping())
print(C.pong(d))
print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
"""改变继承顺序,mro顺序也不一样"""
# (<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
