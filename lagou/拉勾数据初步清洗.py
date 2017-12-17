#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     拉勾数据初步清洗
   Author :       aaa
   date：          2017/12/17
-------------------------------------------------
"""
import re
import codecs

# liststr3 = "北京蚂蜂窝网络科技有限公司 15k-30k 高级Python开发工程师 北京"
# mys = liststr3.split(" ")
# pattern = re.compile(r'^\d{1,2}')
# result = re.findall(pattern, mys[1])
# print(result)

filepath = "F:\\python\\lagou\\lagou1.txt"
file = codecs.open(filepath, "rb", "utf-8", "ignore")
mylist = file.readlines()  # 返回一个list,读取到内存
file.close()

# resultfilepath = r"E:\python\lagou\lagou2.csv"
# filegood = open(resultfilepath, "wb")

pattern = re.compile(r'^\d{1,2}')
with open(r"F:\python\lagou\lagou2.txt", "wb")as f:
    # writer = csv.writer(csvfile)
    # writer.writerow(["company", "salary", "position", "city"])
    for line in mylist:
        linelist = line.split(" ")
        minsalary = re.findall(pattern, linelist[1])
        fcompany = linelist[0]
        fposition = linelist[2]
        fcity = linelist[3]
        if minsalary:
            f.write((fcompany + "," + minsalary[0] + "," + fposition + "," + fcity + '\r\n').encode('utf-8'))
            print("好激动")
