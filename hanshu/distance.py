#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: distance.py
 
@time: 2017/12/2 14:04
 
@desc:
 
'''
import turtle
x1, y1 = eval(input("两个坐标"))
x2, y2 = eval(input("再两个坐标"))
print(x1, y1)

turtle.penup()
turtle.goto(x1,y1)

turtle.pendown()
turtle.goto(x2,y2)

legth=((x1-x2)**2+(y1-y2)**2)**0.5

print(legth)

turtle.done()
