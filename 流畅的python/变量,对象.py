#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
@File    : 变量,对象.py
'''


class Gim:

    def __init__(self):
        print('函数id是%s' % id(self))


x = Gim()
print()
y = Gim() * 10
"""
这里会报错,但还是能打印id,这说明,在求积前会创建对象的实例并调用init方法,
但是没有创建变量y


函数id是48921072
  File "E:/python/流畅的python/变量,对象.py", line 19, in <module>

    y = Gim()*10
函数id是86214544
TypeError: unsupported operand type(s) for *: 'Gim' and 'int'

书上言论
# 为了理解 Python 中的赋值语句， 应该始终先读右边。 对象在
右边创建或获取， 在此之后左边的变量才会绑定到对象上， 这就像
为对象贴上标注。 忘掉盒子吧！
对象一旦创建， 它的标识绝不会
变； 你可以把标识理解为对象在内存中的地址。 is 运算符比较两个
对象的标识； id() 函数返回对象标识的整数表示
"""
print(y)

# l1 = [3, [66, 55, 44], (7, 8, 9)]
# l2 = list(l1) #
# l1.append(100) #
# l1[1].remove(55) #li
# l1[0]=4
# print('l1:', l1)
# print('l2:', l2)
# l2[1] += [33, 22] #
# l2[2] += (10, 11) #
# print('l1:', l1)
# print('l2:', l2)

# 函数参数默认值不要用可变类型



