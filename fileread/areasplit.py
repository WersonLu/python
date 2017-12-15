#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/7 22:55
 
'''

import codecs

filepath = r"E:\study\fileread\kfgood18.txt"
file = codecs.open(filepath, "rb", "utf-8", "ignore")  # 按照指定编码
mylist = file.readlines()  # 返回一个list,读取到内存
file.close()
print("load")
area = [[1, "华北"], [2, "东北"], [3, "华东"], [4, "中南"], [5, "西南"], [6, "西北"]]
areafilelist = []
length = len(area)  # 长度
for data in area:
    kffilepath = "E:\\study\\fileread\\area\\" + data[1] + ".txt"
    kffile = open(kffilepath, "wb")
    areafilelist.append(kffile)

for line in mylist:
    # print(line.split(","))
    linelist = line.split(",")  # 字符串切割
    chstr = linelist[4][0]  # 取出一个字符
    for i in range(length):
        # x = area[i][0]
        # print(x)
        if str(area[i][0]) == chstr:
            areafilelist[i].write(line.encode("utf-8"))
            break
print("over")
for kffile in areafilelist:  # 关闭文件
    kffile.close()
