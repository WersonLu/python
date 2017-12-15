#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/11 16:49
 
'''
import time
import itchat
import datetime
import tushare as ts

stock_symbol = input('请输入股票代码 \n>  ')
price_low = input('请输入最低预警价格 \n>  ')
price_high = input('请输入最高预警价格 \n>  ')


def login():
    itchat.auto_login()


def stock():
    time = datetime.datetime.now()
    now = time.strftime('%H:%M:%S')
    data = ts.get_realtime_quotes(stock_symbol)
    r1 = float(data['price'])
    r2 = str(stock_symbol) + '的当前价格' + str(r1)
    content = now + '\n' + r2
    itchat.send(content, toUserName='filehelper')
    if r1 <= float(price_low):
        itchat.send('低于最低预警价格', toUserName='filehelper')
        print("低于最低价格")
    elif r1 >= float(price_high):
        itchat.send('高于最高预警价格', toUserName='filehelper')
        print("高于最高价格")
    else:
        itchat.send("价格正常", toUserName='filehelper')


if __name__ == '__main__':
    login()
    while True:
        try:
            stock()
            time.sleep(10)
        except KeyboardInterrupt:
            itchat.send('Stock_WeChat 已执行完毕', toUserName='filehelper')
            print('Stock_WeChat 已执行完毕')
            break
