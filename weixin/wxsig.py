#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2018/1/20 15:00
 
'''
import itchat
import re

itchat.login()

friends = itchat.get_friends(update=True)[0:]
for i in friends:
    signature = i["Signature"].strip().replace("span", "").replace("class", "")
    rep = re.compile("1f\d.+")
    signature = rep.sub("", signature)
    print(signature)
