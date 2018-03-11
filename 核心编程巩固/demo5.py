#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
@File    : demo4.py
'''

"""
类
"""


class C2: ...


class C3: ...


class C1(C2, C3):

    def setname(self, who):
        self.name = who


i1 = C1()
i2 = C1()
i1.setname('bod')
print(i1.name)


# 实例

class Person:
    # self 新创建的实例对象
    # def __init__(self, name, age, job):
    #     self.name = name
    #     self.age = age
    #     self.job = job
    #  在python中,第一个拥有默认值的参数之后的任何参数,都必须用于默认值

    # 构造函数
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.pay = pay
        self.job = job

    def last_name(self):
        return self.name.split()[1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    # 自带的方法 来构建显示字符串  用户友好显示
    def __str__(self):
        return '[Person:%s,%s,%s]' % (self.name, self.job, self.pay)

    # 开发者友好显示
    def __repr__(self):
        pass


class Manager(Person):

    def give_raise(self, percent, bonus=.10):
        # self.pay = int(self.pay * (1 + percent + bonus))
        # 好的扩展方法
        Person.give_raise(self, percent + bonus)


if __name__ == '__main__':
    bob = Person('liu wei')
    print(bob.name, bob.pay)
    sue = Person('刘立', job='dev', pay=1000)
    print(sue.pay)
    """
    当代码作为模块导入的时候,它的顶层print语句会运行,但我们不想它
    打印出测试输出.所以此时要使用到__name__检查模块
    """
    print(bob.name.split()[1])
    sue.pay *= 1.1
    print(sue.pay)

    tom = Manager('Tom Jon', 'enginer', 5000)
    tom.give_raise(.10)
    print(tom, tom.last_name())

    # 多态的表现
    for obj in (bob, sue, tom):
        obj.give_raise(.10)
        print(obj)

print("...........")


class Person1:
    # 构造函数
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.pay = pay
        self.job = job

    def last_name(self):
        return self.name.split()[1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    # 自带的方法 来构建显示字符串  用户友好显示
    def __str__(self):
        return '[Person:%s,%s,%s]' % (self.name, self.job, self.pay)

    # 开发者友好显示
    def __repr__(self):
        pass


class Manager1(Person1):
    # 定制自己的构造函数
    def __init__(self, name, pay):
        Person1.__init__(self, name, 'dev', pay)

    def give_raise(self, percent, bonus=.10):
        # self.pay = int(self.pay * (1 + percent + bonus))
        # 好的扩展方法
        Person1.give_raise(self, percent + bonus)


if __name__ == '__main__':
    bob = Person1('liu wei')
    print(bob.name, bob.pay)
    sue = Person1('刘立', job='dev', pay=1000)
    print(sue.pay)
    """
    当代码作为模块导入的时候,它的顶层print语句会运行,但我们不想它
    打印出测试输出.所以此时要使用到__name__检查模块
    """

    tom = Manager1('Tom Jon', 5000)
    tom.give_raise(.10)
    print(tom, tom.last_name())
"""
1.实例创建
2.行为方法
3.运算符重载
4.定制行为
5.定制构造函数

"""
