#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     递归文件函数
   Author :       aaa
   date：          2017/12/14
-------------------------------------------------
"""
import os


# 用文件树遍历文件夹   深度遍历
# filepath = os.listdir(r"G:\photo-照片")
#
# for file in filepath:
#     if os.path.isdir("G:\\photo-照片\\" + file):
#         print("是文件夹", file)
#     else:
#         print("文件", file)
def getall(path, treeshow):
    treeshow += "    "
    filelist = os.listdir(path)
    for file in filelist:
        # 把两个拼接 join
        filename = os.path.join(path, file)
        # 是文件夹继续遍历
        if os.path.isdir(filename):
            print(treeshow, "文件夹", file)
            getall(filename, treeshow)
        else:
            print(treeshow, "这是文件", file)


getall(r"F:\workspace", treeshow="    ")

# import os
# path=r"C:\Users\Tsinghua-yincheng\Desktop\day19"
# mystack=[]
# mystack.append([path,0])
#
# while  len(mystack)!=0:
#     pathlist=mystack.pop()#取出路径与层次
#     filelist=os.listdir(pathlist[0]) #遍历路径
#
#     num=pathlist[1]#代表层次
#     headstr=""
#     for  i  in range(num): #控制层次感
#         headstr+="      "
#
#     #for filename in filelist:
#     for i in range(len(filelist)):
#         filename=filelist[len(filelist)-1-i]
#         filepath = os.path.join(pathlist[0], filename)  # 链接，取得绝对路径
#         if os.path.isdir(filepath):#文件夹
#             print(headstr,"文件夹", filepath)
#             mystack.append([filepath,num+1])
#         else:#文件
#             print(headstr,"文件",filepath)
