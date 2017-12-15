#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: toutiao.py
 
@time: 2017/12/5 13:27
 
@desc:
 
'''
import requests
import json
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='51job', charset='utf8')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS DATA")

sqlc = """
    CREATE TABLE data (
        Title VARCHAR(100) ,
        URL VARCHAR(100),
        IMG_URL VARCHAR(100))DEFAULT CHARSET=utf8;

"""

try:
    A = cursor.execute(sqlc)
    conn.commit()
    print('成功')
except:
    print("错误")

url = 'http://www.toutiao.com/api/pc/focus/'
wbdata = requests.get(url).text

data = json.loads(wbdata)
news = data['data']['pc_feed_focus']

for n in news:
    title = n['title']
    utl = n['media_url']
    img_url = n['image_url']
    print(title, url, img_url)
    data_new = (title, url, img_url)

    cursor.execute("INSERT INTO DATA (title,url,img_url,)VALUES(%s,%s,%s),", data_new)
    conn.commit()
cursor.close()
conn.close()
