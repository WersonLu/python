#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2018/1/29 2:05
 
'''
import re
import itchat
import time
import requests
from lxml import etree


def login():
    itchat.auto_login()


def getMoney():
    url = 'http://www.boc.cn/sourcedb/whpj/index.html'
    html = requests.get(url).content.decode('utf-8')

    a = html.index('<td>美元</td>')  # 取得“新西兰元”当前位置
    s = html[a:a + 300]  # 截取新西兰元汇率那部分内容（从a到a+300位置）
    result = re.findall('<td>(.*?)</td>', s)  # 正则获取
    # print(result)

    content = str('名称:' + result[0] + '\n'
                  + '现汇买入:' + result[1] + '\n'
                  + '现钞买入:' + result[2] + '\n'
                  + '现汇卖出:' + result[3] + '\n'
                  + '现钞卖出:' + result[4] + '\n'
                  + '中国银行折算:' + result[5] + '\n'
                  + '时间:' + result[6] +''+ result[7] + '\n')
    itchat.send(content, toUserName='filehelper')


if __name__ == '__main__':
    login()
    while True:
        try:
            getMoney()
            # 自己设定多久执行一次单位秒
            time.sleep(10)

        except KeyboardInterrupt:  # 用户中断执行
            print('用户终止程序')
            break
