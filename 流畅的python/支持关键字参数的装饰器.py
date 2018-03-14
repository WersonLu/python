#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
@File    : 支持关键字参数的装饰器.py
'''

import time
import functools


# 这个装饰器 返回函数运行时间和函数在内存的id
def clock(func):
    @functools.wraps(func)  # 这个系统装饰器可以把相关的属性从func复制到clocked去
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        id_fun = id(func)
        arg_list = []
        if args:
            arg_list.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, v) for k, v in sorted(kwargs.items())]
            arg_list.append(', '.join(pairs))
        arg_str = ', '.join(arg_list)
        print('[%0.8fs] %s(%s)%r -> %r ' % (elapsed, name, id_fun, arg_str, result))
        return result

    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def fu(m):
    return 1 if m < 2 else m * fu(m - 1)


# 这个装饰器可以接受配置参数
@functools.lru_cache()
# @clock
def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)


if __name__ == '__main__':
    print('>>>>>', 'calling snooze(5)')
    snooze(5)
    print('>>>>>', 'calling')
    print(fu(6))
    print(fib(9))

# 这是做备忘的装饰
