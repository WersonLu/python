#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     一个常用的工具类
   Author :       aaa
   date：          2017/12/17
-------------------------------------------------
"""
#
import os


class Deal:
    def __init__(self):
        self.path = ""
        if not self.path.endswith('/'):
            self.path = self.path + '/'
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def mkDir(self, path):
        path = path.strip()
        dir_path = self.path + path
        exists = os.path.exists(dir_path)
        if not exists:
            os.makedirs(dir_path)
            return dir_path
        else:
            return dir_path

    def saveImg(self, content, path):
        f = open(path, 'wb')
        f.write(content)
        f.close()

    def saveBrief(self, content, dir_path, name):
        file_name = dir_path + "/" + name + ".txt"
        f = open(file_name, "w+")
        f.write(content.encode('utf-8'))

    def getExtension(self, url):
        extension = url.split('.')[-1]
        return extension

# 这里面包含了四个方法。
#
# mkDir：创建文件夹，用来创建
# MM
# 名字对应的文件夹。
#
# saveBrief: 保存简介，保存
# MM
# 的文字简介。
#
# saveImg: 传入图片二进制流以及保存路径，存储图片。
#
# getExtension: 获得链接的后缀名，通过图片
# URL
# 获得。
