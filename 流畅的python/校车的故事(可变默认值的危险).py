#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
@File    : 校车的故事(可变默认值的危险).py
'''


class Bus:
    # ide已经给出了异常提示,
    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


b1 = Bus(['流量', '移动'])
print(b1.passengers)  # ['流量', '移动']
b1.pick('联通')
b1.drop('移动')
print(b1.passengers)  # ['流量', '联通']

bus2 = Bus()
# 上车
bus2.pick('Carrie')
print(bus2.passengers)  # ['Carrie']

b3 = Bus()
print(b3.passengers)  # ['Carrie'] 很恐怖,这个人竟然上车了
b3.pick('电信')

print(bus2.passengers, b3.passengers)  # ['Carrie', '电信'] ['Carrie', '电信']
"""
实例化 HauntedBus 时， 如果
传入乘客， 会按预期运作。 但是不为 HauntedBus 指定乘客的话， 奇怪
的事就发生了， 这是因为 self.passengers 变成了 passengers 参数默认值的别名

为什么会上面这样,没有指定初始乘客的bus实例会共享同一个乘客列表
默认值在定义函数时计算（ 通常在加载模块时)，默认值变成了函数对象的属性。 
因此，如果默认值是可变对象，而且修改了它的值，那么后续的函数调用都会受到影响。
"""
print(b1.passengers)  # ['流量', '联通']

print(Bus.__init__.__defaults__)  # (['Carrie', '电信'],)
