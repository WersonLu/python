#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/8 11:35
 
'''

# 按照出身年份切割
import codecs

filepath = r"E:\study\fileread\kfgood18.txt"
file = codecs.open(filepath, "rb", "utf-8", "ignore")  # 按照指定编码
mylist = file.readlines()  # 返回一个list,读取到内存
file.close()
print("load")

area = [x for x in range(1900, 2018)]
print(area)
areafilelist = []
length = len(area)  # 长度
for data in area:
    kffilepath = "E:\\study\\fileread\\age\\" + str(data) + ".txt"
    kffile = open(kffilepath, "wb")
    areafilelist.append(kffile)

for line in mylist:
    linelist = line.split(",")  # 字符串切割
    chstr = linelist[4][6:10]  # 取出4个字符
    for i in range(length):
        if str(area[i]) == chstr:
            areafilelist[i].write(line.encode("utf-8"))
            break

print("over")
for kffile in areafilelist:  # 关闭文件
    kffile.close()
