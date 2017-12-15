#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/11 14:30
 
'''
import itchat
import time
import requests
import threading
from bs4 import BeautifulSoup


def login():
    itchat.auto_login()


def gupiao():
    pass  # 股票监控,其他监控


def getPM25(cityname):
    site = 'http://www.pm25.com/' + cityname + '.html'
    html = requests.get(site).text
    soup = BeautifulSoup(html, 'lxml')
    # 用soup的find方法匹配出符合的数据,取出文本
    city = (soup.find(class_="bi_loaction_city")).text
    aqi = (soup.find("a", {"class", "bi_aqiarea_num"})).text
    quality = (soup.find(class_="wuranlevel_2")).text
    result = (soup.find(class_="bi_aqiarea_bottom")).text
    sheshidu = (soup.find(class_="bi_info_weather")).text
    # 转为字符串作为参数用itchat推送
    content = str(city + u'aqi指数' + aqi + u'空气质量:' + quality + result + sheshidu)
    # itchat把信息推送给文件助手
    itchat.send(content, toUserName='filehelper')


def two_thread():
    threads = []  # 线程池
    t1 = threading.Thread(target=getPM25, args=('wuhan',))  # 自己要查询的城市的拼音
    threads.append(t1)
    t2 = threading.Thread(target=getPM25, args=('shenzhen',))
    threads.append(t2)
    t3 = threading.Thread(target=getPM25, args=('hengyang',))
    threads.append(t3)

    for t in threads:
        t.start()


if __name__ == '__main__':
    login()
    while True:
        try:
            two_thread()
            # 自己设定多久执行一次单位秒
            time.sleep(3600)
        except KeyboardInterrupt:  # 用户中断执行
            print('用户终止程序')
            break
