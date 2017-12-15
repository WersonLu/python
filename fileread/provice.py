#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/7 23:32
 
'''

import codecs

filepath = r"E:\study\fileread\kfgood18.txt"
file = codecs.open(filepath, "rb", "utf-8", "ignore")  # 按照指定编码
mylist = file.readlines()  # 返回一个list,读取到内存
file.close()
print("load")

area = [[11, "北京"], [12, "天津"], [13, "河北"], [14, "山西"], [15, "内蒙古"], [21, "辽宁"], [22, "吉林"], [23, "黑龙江"], [31, "上海"],
        [32, "江苏"], [33, "浙江"], [34, "安徽"], [35, "福建"], [36, "江西"], [37, "山东"], [41, "河南"], [42, "湖北"],
        [43, "湖南"], [44, "广东"], [45, "广西"], [46, "海南"], [50, "重庆"],
        [51, "四川"], [52, "贵州"], [53, "云南"], [54, "西藏"], [61, "陕西"],
        [62, "甘肃"], [63, "青海"], [64, "宁夏"], [65, "新疆"], [71, "台湾"],
        [81, "香港"], [82, "澳门"]]
areafilelist = []
length = len(area)  # 长度
for data in area:
    kffilepath = "E:\\study\\fileread\\province\\" + data[1] + ".txt"
    kffile = open(kffilepath, "wb")
    areafilelist.append(kffile)

for line in mylist:
    linelist = line.split(",")  # 字符串切割
    chstr = linelist[4][0:2]  # 取出2个字符
    for i in range(length):
        if str(area[i][0]) == chstr:
            areafilelist[i].write(line.encode("utf-8"))
            break

print("over")

for kffile in areafilelist:  # 关闭文件
    kffile.close()
