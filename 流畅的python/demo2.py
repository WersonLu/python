#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com

'''

from math import hypot

"""
一个向量类
"""

"""
__repr__和__str__这两个方法都是用于显示的，__str__是面向用户的，而__repr__面向程序员。

打印操作会首先尝试__str__和str内置函数(print运行的内部等价形式)，它通常应该返回一个友好的显示。

__repr__用于所有其他的环境中：用于交互模式下提示回应以及repr函数，如果没有使用__str__，会使用print和str。
它通常应该返回一个编码字符串，可以用来重新创建对象，或者给开发者详细的显示。

当我们想所有环境下都统一显示的话，可以重构__repr__方法；当我们想在不同环境下支持不同的显示，
例如终端用户显示使用__str__，而程序员在开发期间则使用底层的__repr__来显示，实际上__str__只是覆盖了__repr__以得到更友好的用户显示。
"""


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r,%r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, other):
        return Vector(self.x * scalar, self.y * scalar)


v1 = Vector(2, -6)
v2 = Vector(3, 8)
print(v2 + v1)
# 通过特殊方法,自定义数据类型可以表现得像内置类型一样

