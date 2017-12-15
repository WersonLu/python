#!/usr/bin/env python

# encoding: utf-8

'''
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/7 17:09
 
'''

# 一个数据库查询demo
import pymysql

connection = pymysql.connect(host="localhost", user="root",
                             password="root", db="world", port=3306)
cur = connection.cursor()
sql = "select * from city"


def query(sql):
    try:
        cur.execute(sql)
        results = cur.fetchall()
        for row in results:
            id = row[0]
            name = row[1]
            countrycode = row[2]
            district = row[3]
            population = row[4]
            print(id, name, countrycode, district, population)
    except Exception as  e:
        connection.rollback()
        raise e
    finally:
        connection.close()


if __name__ == "__main__":

    while True:
        sql = input("请输入查询语句")
        query(sql)