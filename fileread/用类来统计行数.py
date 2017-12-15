#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/8 16:00
 
'''


class filegetlines:
    # 数据
    def __init__(self, filepath):
        self.filepath = filepath
        self.file = open(filepath, "rb")
        self.Lines = -1

    # 行为
    def readlines(self):
        i = 0
        while True:
            linestr = self.file.readline()
            if linestr:
                print(linestr)
                i += 1
            else:
                break
        self.Lines = i
        return i


f1 = filegetlines("3.txt")
f1.readlines()
print(f1.readlines())
