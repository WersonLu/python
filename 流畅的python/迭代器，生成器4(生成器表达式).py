#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
@File    : 迭代器，生成器4(生成器表达式).py
'''

import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))


"""
这里不是生成器函数了
（ 没有 yield） ， 而是使用生成器表达式构建生成器， 然后将其返回。
不过， 最终的效果一样： 调用 __iter__ 方法会得到一个生成器对象。
"""
