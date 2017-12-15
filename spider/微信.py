#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/13 12:23
 
'''
from wxpy import *

rob = Bot()

a = rob.chats()

Friends = rob.friends()
print(Friends.stats_text())

group = rob.groups()
for x in group:
    print(x)
