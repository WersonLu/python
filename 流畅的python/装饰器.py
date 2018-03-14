#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
@File    : 装饰器.py
'''
res = []


def register(func):
    print('running register(%s)' % func)
    res.append(func)
    return func


@register
def f1():
    print('f1函数正运行')


def main():
    print('主函数正运行')
    print('register->', register)
    f1()


if __name__ == '__main__':
    main()
