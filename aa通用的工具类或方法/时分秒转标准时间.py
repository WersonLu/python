#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
@File    : 时分秒转标准时间.py
'''
import time


def calc_date(s):
    words = {u'小时': 3600, u'分钟': 60, u'秒': 1}
    second = 0
    for k, v in words.items():
        temp = s.split(k)
        if len(temp) == 2:
            second = int(temp[0]) * v
            break
    if second != 0:
        return time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time() - second))
    else:
        return s.replace(u'年', '-').replace(u'月', '-').replace(u'日', '')
