#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/7 18:28
 
'''
# 初步数据清洗
import codecs

filepath = r"E:\study\fileread\kaifang.txt"
file = codecs.open(filepath, "rb", "utf-8", "ignore")  # 按照指定编码
mylist = file.readlines()  # 返回一个list,读取到内存
file.close()

savegoodfilepath = r"E:\study\fileread\kaifanggood.txt"
savebadfilepath = r"E:\study\fileread\kaifangbad.txt"
filegood = open(savegoodfilepath, "wb")
filebad = open(savebadfilepath, "wb")
for line in mylist:
    # print(line.split(","))
    # print()
    linelist = line.split(",")
    if len(linelist) >= 20:
        if len(linelist[19]) == 11 and len(linelist[4]) == 18 and len(linelist[7]) >= 1:
            # good 姓名 电话 身份证号
            filegood.write(
                (linelist[0] + " " + linelist[19] + " " + linelist[4] + " " + linelist[7] + "\n").encode("utf-8"))
            pass
        else:
            # bad
            filebad.write(line.encode("utf-8"))
            pass
    else:
        # bad
        filebad.write(line.encode("utf-8"))
        pass

filebad.close()
filegood.close()
# 成功分割成好的数据kfgood18,并且分割出手机号
