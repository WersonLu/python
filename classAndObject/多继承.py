#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/13 15:35
 
'''


class 爹:
    def __init__(self):
        # 用_修饰的私有变量不可继承
        self._wife = "娘"


class 儿(爹):
    def __init__(self):
        super().__init__()
        print(self._wife)


class 美女演员的亲爹:
    def __init__(self):
        self.money = 1000
        self.bike = "自行车"
        self.live = "天桥下"

    def buy(self):
        print("买不起车买不起房")

    def do(self):
        print("农民")


class 美女演员的干爹:
    def __init__(self):
        self.money = 20000000
        self.car = "兰博基尼"
        self.house = "天宫"

    def bigbuy(self):
        print("什么都能买")

    def do(self):
        print("土豪")


# 继承两个类
class 美女演员(美女演员的亲爹, 美女演员的干爹):
    def __init__(self):
        # 初始化
        美女演员的亲爹.__init__(self)
        美女演员的干爹.__init__(self)

    def wanto(self):
        print("可以潜规则,必须有钱")


dawang = 爹()
print(dawang._wife)

# 多继承,同时继承两个类的属性方法

jt = 美女演员()
print(jt.buy())
jt.bigbuy()
jt.buy()
print(jt.money)  # 干爹覆盖了亲爹   属性后面覆盖前面 ,但是跟初始化顺序有关.
print(jt.do())  # 亲爹覆盖了干爹     方法前面覆盖后面,跟继承顺序有关

# 属性是每个对象私有,方法是共享
# 所有类都是object的子孙

# 类的特殊属性
# class .__doc__ 类的说明
#
# class .__module__类从哪个地方执行
#
# class .__dict__类的所有属性放在字典
