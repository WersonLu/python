#!/usr/bin/env python

# encoding: utf-8

'''
@author: wersonliu
@contact: wersonliugmail.com
@time: 2017/12/5 12:25
'''
import requests

# 打开一个文件,wb模式写入数据
f = open("lagou1.txt", "wb")
for i in range(1, 50):
    # 通过循环来改变pageNo的值
    # 如果已知url是json,不用.text或者 get_text
    response = requests.get(
        'https://m.lagou.com/search.json?'
        'city=%E5%85%A8%E5%9B%BD&positionName=python&pageNo='
        + str(i) + '&pageSize=15')
    # 懂json的这里就很容易理解的
    arr = response.json()['content']['data']['page']['result']
    for n in arr:
        address = n['city']
        company = n['companyFullName']
        salary = n['salary']
        job = n['positionName']
        # 文件写入
        f.write((company + ' ' + salary + ' ' + job + ' ' + address + "\r\n").encode('utf-8'))
        # 控制台打印
        print(company + '|' + salary + '|' + job + '|' + address + '\n')
# 关闭文件流
f.close()
