#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2018/1/19 16:33
 
'''
import urllib3
import time, requests, urllib, json, re
from bs4 import BeautifulSoup
from lxml import etree
from collections import OrderedDict
import pandas as pd
import xlwt

import sys


def getPage(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    try:
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request, timeout=5)
        page = response.read().decode('utf-8')
        return page
    except urllib.error.URLError as e:
        if hasattr(e, 'reason'):
            print('抓取失败，具体原因：', e.reason)
            request = urllib.request.Request(url=url, headers=headers)
            response = urllib.request.urlopen(request, timeout=5)
            page = response.read().decode('utf-8')
            return page


def getList():
    place = input("请输入地点")
    url = 'http://piao.qunar.com/ticket/list_' + str(
        place) + '.html?in_track=index_tab_remcs&from=qunar&keyword=' + str(place) + '&page={}'
    i = 1
    sightlist = []
    while i < 2:
        page = getPage(url.format(i))
        selector = etree.HTML(page)
        print("第" + str(i) + '页数据')
        i += 1
        inforations = selector.xpath('//div[@class="result_list"]/div')
        for inf in inforations:
            sight_name = inf.xpath('./div/div/h3/a/text()')[0]
            sight_level = inf.xpath('.//span[@class="level"]/text()')
            if len(sight_level):
                sight_level = sight_level[0].replace('景区', '')
            else:
                sight_level = 0
            # 地区 //*[@id="search-list"]/div[1]/div/div[2]/div/div[1]/span
            sight_area = inf.xpath('.//span[@class="area"]/a/text()')[0]

            sight_hot = inf.xpath('.//span[@class="product_star_level"]//span/text()')[0].replace('热度 ', '')
            # 地址
            sight_add = inf.xpath('.//p[@class="address color999"]/span/text()')[0]
            sight_add = re.sub('地址：|（.*?）|\(.*?\)|，.*?$|\/.*?$', '', str(sight_add))
            # 口号
            sight_slogen = inf.xpath('.//div[@class="intro color999"]/text()')[0]
            sight_price = inf.xpath('.//span[@class="sight_item_price"]/em/text()')
            if len(sight_price):
                sight_price = sight_price[0]
            else:
                i = 0
                break
            sight_soldnum = inf.xpath('.//span[@class="hot_num"]/text()')[0]
            sight_point = inf.xpath('./@data-point')[0]
            print(sight_point)
            sight_url = inf.xpath('.//h3/a[@class="name"]/@href')[0]
            sightlist.append(
                [sight_name, sight_level, sight_area, float(sight_price), int(sight_soldnum), float(sight_hot),
                 sight_add.replace('地址：', ''), sight_point, sight_slogen, sight_url])
            time.sleep(3)
    return sightlist, place


def listtoExcel(list, name):
    df = pd.DataFrame(list, columns=['景点名称', '级别', '所在区域', '起步价', '销售量', '热度', '地址', '经纬度', '标语', '详情网址'])
    df.to_excel(name + '景点信息.xlsx')


def datatojson(slightlist):
    json_geo={}
    bjsonlist=[]
    ejsonlist1=[]
    ejsonlist2=[]
    num=1
    for l in slightlist:
        p='(.*?),(.*?)$'


