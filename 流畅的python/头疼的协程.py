#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
@File    : 头疼的协程.py
'''

# 先说简介
"""
协程与生成器类似， 都是定义体中包含 yield 关键字的
函数。 可是， 在协程中， yield 通常出现在表达式的右边（ 例
如， datum = yield） ， 可以产出值， 也可以不产出——如果 yield
关键字后面没有表达式， 那么生成器产出 None。 协程可能会从调用方
接收数据， 不过调用方把数据提供给协程使用的是 .send(datum) 方
法， 而不是 next(...) 函数。 通常， 调用方会把值推送给协程。

yield  控制流程 
关键字还可以不接收或传出数据
协程 可以把控制器让步给中心调度程序,从而激活其他协程
"""
