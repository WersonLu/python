#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
@File    : 参数化装饰器.py
'''
import time

registry = []


def register(func):
    print('register(%s) 正在跑' % func)
    registry.append(func)
    return func


@register
def f1():
    print("f1 正在跑")


# if __name__ == '__main__':
#     f1()
"""
一个装饰器工厂函数
"""

# registry1 = set()

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

"""
参数化装饰器 工厂函数
"""


# 工厂函数
def register1(fmt=DEFAULT_FMT):
    def decorate(func):  # 装饰器 参数是函数
        def clocked(*args):
            to = time.time()
            result = func(*args)  # 函数的返回值
            elapsed = time.time() - to
            name = func.__name__
            args = ', '.join(repr(arg) for arg in args)
            _result = repr(result)  # 函数返回值的字符串变现形式
            print(fmt.format(**locals()))
            """
            locals函数的用法:把之前的所有局部变量转为字典并返回,传给format函数结构使用
            """
            return _result

        return clocked

    return decorate


if __name__ == '__main__':
    @register1('{name}:{elapsed}s')
    def f2(seconds):
        time.sleep(seconds)


    for i in range(4):
        f2(i)
