#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2018/2/1 9:36
 
'''
# 类的属性和方法

class FirstClass:
    def setDate(self, value):
        self.date = value

    def display(self):
        print(self.date)


x = FirstClass()
# y = FirstClass()
x.setDate('liuwei')
x.display()
x.setDate('new value')
x.display()


class SecondClass(FirstClass):
    def display(self):
        print('Current value="%s"' % self.date)


z = SecondClass()
z.setDate(56)
z.display()
x.display()


class Rec:
    pass


Rec.name = 'Bob'
print(Rec.name)
x = Rec()
y = Rec()
print(x.name)
x.name = 'Sur'
print(Rec.name, x.name, y.name)
print(Rec.__dict__.keys())
print(x.__dict__.keys())
print(y.__dict__.keys())


# 转为大写的方法
def UpperName(self):
    return self.name.upper()


Rec.method = UpperName
print(x.method())
print(y.method())
print(Rec.method(x))