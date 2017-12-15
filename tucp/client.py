#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: client.py
 
@time: 2017/12/6 9:40
 
@desc:
 
'''
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print('--->' + s.recv(1024).decode('utf-8'))
s.send(b'hello')
print('-->' + s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
