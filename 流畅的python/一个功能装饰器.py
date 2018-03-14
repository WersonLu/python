#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
@File    : 一个功能装饰器.py
'''

import time


def clock(func):  # 自由变量func
    def clocked(*args):  # 闭包
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ','.join(repr(arg) for arg in args)
        print('[%0.8fs]%s(%s)->%r' % (elapsed, name, arg_str, result))
        return result

    """会遮挡被装饰函数的__name__,__doc__属性"""
    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def fu(m):
    return 1 if m < 2 else m * fu(m - 1)


if __name__ == '__main__':
    print('>>>>>', 'calling snooze(5)')
    snooze(5)
    print('>>>>>', 'calling')
    print(fu(6))
"""
装饰器的典型行为:把被装饰的函数替换成新函数,二者接受相同的参数,而且返回被装饰的函数本该返回的值,还可以有其他操作
"""


