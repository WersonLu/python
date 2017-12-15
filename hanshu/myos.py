#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: myos.py
 
@time: 2017/12/2 11:37
 
@desc:
 
'''
import turtle

turtle.color("blue")
turtle.circle(100)


turtle.penup() #抬笔
turtle.goto(-200, 0)
turtle.pendown()
turtle.color("red")
turtle.circle(100)

turtle.penup()
turtle.goto(200, 0)
turtle.pendown()
turtle.color("black")
turtle.circle(100)

turtle.penup() #抬笔
turtle.goto(-200,-100)
turtle.pendown()
turtle.color("yellow")
turtle.circle(100)

turtle.done()
