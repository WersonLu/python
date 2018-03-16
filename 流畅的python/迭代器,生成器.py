#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
@File    : 迭代器,生成器.py
'''
import re
import reprlib

"""
在 Python 中， 所有集合都可以迭代。 在 Python 语言内部， 迭代器用于
支持：
for 循环
构建和扩展集合类型
逐行遍历文本文件
列表推导、 字典推导和集合推导
元组拆包
调用函数时， 使用 * 拆包实参

语言内部使用 iter(...) 内置函数处理可迭代对象的方式
如何使用 Python 实现经典的迭代器模式
详细说明生成器函数的工作原理
如何使用生成器函数或生成器表达式代替经典的迭代器
如何使用标准库中通用的生成器函数
如何使用 yield from 语句合并生成器
案例分析： 在一个数据库转换工具中使用生成器函数处理大型数据
集 为
什么生成器和协程看似相同， 实则差别很大， 不能混淆
首先来研究 iter(...) 函数如何把序列变得可以迭代。
"""
# 预编译正则
RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        # 用于生成大型数据结构的简略字符串表示形式
        return 'Sentence%s' % reprlib.repr(self.text)


s = Sentence("i love you ,can you help me")
print(s)
print(s[0])
"""
序列可以迭代的原因： iter函数
解释器需要迭代对象 x 时， 会自动调用 iter(x)。
内置的 iter 函数有以下作用。
(1) 检查对象是否实现了 __iter__ 方法， 如果实现了就调用它， 获取
一个迭代器。
(2) 如果没有实现 __iter__ 方法， 但是实现了 __getitem__ 方法，
Python 会创建一个迭代器， 尝试按顺序（ 从索引 0 开始） 获取元素。
(3) 如果尝试失败， Python 抛出 TypeError 异常， 通常会提示“C object
is not iterable”（ C 对象不可迭代） ， 其中 C 是目标对象所属的类。
"""

"""
可迭代的对象
使用 iter 内置函数可以获取迭代器的对象。 如果对象实现了能返
回迭代器的 __iter__ 方法， 那么对象就是可迭代的。 序列都可以迭
代； 实现了 __getitem__ 方法， 而且其参数是从零开始的索引， 这种
对象也可以迭代。
我们要明确可迭代的对象和迭代器之间的关系： Python 从可迭代的对象
中获取迭代器。

for 循环什么时候中止迭代,内部 stopiteration异常
迭代器无法还原,想再次迭代,需要调用iter
"""

"""
迭代器是这样的对象： 实现了无参数的 __next__ 方法， 返回序列
中的下一个元素； 如果没有元素了， 那么抛出 StopIteration 异常。
Python 中的迭代器还实现了 __iter__ 方法， 因此迭代器也可以迭代。
因为内置的 iter(...) 函数会对序列做特殊处理， 所以第 1 版
Sentence 类可以迭代。 接下来要实现标准的可迭代协议。

"""
