#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/8 10:22
 
'''
import re

liststr3 = "北京蚂蜂窝网络科技有限公司 15k-30k 高级Python开发工程师 北京"
mys = liststr3.split(" ")
pattern = re.compile(r'^\d{1,2}')
result = re.findall(pattern, mys[1])
print(result)
# print(mys)
# ['15']
# ['北京蚂蜂窝网络科技有限公司', '15k-30k', '高级Python开发工程师', '北京']

# linstr = "456or213 # 15821 # wersonliu@163.com"
# mylist = linstr.split(" # ")
# print(mylist)  # 打印列表
# print(mylist[2])
# listr2 = "李艳芳,,,ID,371522199010256028,F,19901025,涧西区文兴现代城2—906室洛阳亿美网络技术有限公司,471003,,,CHN,,,,,,LI YAN FANG,,15539736319,06357662788,,,,,,洛阳亿美网络技术有限公司,,,,0,2013-1-5 9:30:42,20042078"
# mylist2 = listr2.split(",")
# print(mylist2)
# print(mylist2[19])
# print(mylist2[0])
# print(mylist2[7])
# print(mylist2)
# # print(len(mylist2))
# # print(mylist2[0])
# mylist3 = mylist2[0].split(",")
# # print(mylist3)
# # print(len(mylist3))
# print(mylist3[4])
# mylistx=listr2.split(",")
# print(len(mylistx))
# print(mylistx[4])
