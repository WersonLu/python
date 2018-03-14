#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
@File    : 闭包.py
'''


class Averager():

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append((new_value))
        total = sum(self.series)
        return total / len(self.series)


avg = Averager()
print(avg(10))


# 函数式表示

def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


# 效率更高的写法
def make_averager1():
    count = 0
    total = 0

    def averager1(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager1
print(make_averager1())
