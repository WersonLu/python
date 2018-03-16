#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
@File    : 迭代器,生成器2.py
'''

import re
import reprlib

RE_WORD = re.compile("\w+")


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence%s' % reprlib.repr(self.text)

    # 这个方法,明确指明这个对象可迭代
    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceIterator:

    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self


s1 = Sentence("w ai ni zhong guo")
for s in s1:
    print(s)

"""
迭代器模式可用来：
访问一个聚合对象的内容而无需暴露它的内部表示
支持对聚合对象的多种遍历
为遍历不同的聚合结构提供一个统一的接口（ 即支持多态迭
代）

可迭代的对象一定不能是自身的迭代器。 也就是说， 可迭代的对象
必须实现 __iter__ 方法， 但不能实现 __next__ 方法。
另一方面， 迭代器应该一直可以迭代。 迭代器的 __iter__ 方法应
该返回自身
"""
