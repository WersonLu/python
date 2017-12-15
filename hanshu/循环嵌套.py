#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: 循环嵌套.py
 
@time: 2017/12/4 10:45
 
@desc:
 
'''
import turtle

turtle.showturtle()
step = 20
for i in range(11):
    turtle.penup()
    turtle.goto(0, step * i)
    turtle.pendown()
    turtle.forward(step * 11)

turtle.right(270)
for i in range(11):
    turtle.penup()
    turtle.goto(step * i, 0)
    turtle.pendown()
    turtle.forward(step * 10)
turtle.dot(10,"black")
turtle.done
