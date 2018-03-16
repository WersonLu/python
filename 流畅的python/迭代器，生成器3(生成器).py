#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
@File    : 迭代器，生成器3(生成器).py
'''
import re
import reprlib

RE_WORD = re.compile("\w+")


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'sentence%s' % reprlib.repr(self.text)

    """
    只要 Python 函数的定义体中有 yield 关键字， 该函数就是生成器函
    数。 调用生成器函数时， 会返回一个生成器对象。 也就是说， 生成器函
    数是生成器工厂
    """

    def __iter__(self):
        for word in self.words:
            yield word
        return


s1 = Sentence("w ai ni zhong guo")
print(s1.__iter__())


def gen_123():
    yield 1
    yield 2
    yield 3


print(gen_123())
