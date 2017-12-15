#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: 中文命令.py
 
@time: 2017/12/2 17:14
 
@desc:
 
'''
import os
cmdstr=input("输入指令")
if  cmdstr=="记事本":
    os.system("notepad")
elif  cmdstr=="计算器":
    os.system("calc")
elif cmdstr=="进程":
    os.system("tasklist")
elif cmdstr=="IP地址":
    os.system("ipconfig")
elif cmdstr=="重启":
    os.system("shutdown -r -t 200")
elif cmdstr=="关机":
    os.system("shutdown -s -t 200")
else:
    print("其他指令，还没翻译")
