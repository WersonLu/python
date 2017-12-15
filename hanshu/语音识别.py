#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: 语音识别.py
 
@time: 2017/12/2 17:41
 
@desc:
 
'''
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SPVOICE")
speaker.Seak("我是刘伟")
