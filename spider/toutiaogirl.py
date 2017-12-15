#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/9 17:58
 
'''
import requests
from bs4 import BeautifulSoup

with open("boos.txt", "wb") as f:
    for i in range(1, 15):
        url = 'https://www.zhipin.com/c101280600/h_101280600/?query=python&page=' + str(i) + '&ka=page-' + str(i)
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Host': 'www.zhipin.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        }
        a = requests.get(url, headers=headers)
        soup = BeautifulSoup(a.text, 'lxml')
        source1 = soup.find_all("div", class_="job-primary")
        for n in source1:
            company = n.get_text(" ", strip=True)
            f.write(company.encode('utf-8'))
            companyList = company.strip("").split(" ")
            print(companyList)
f.close()
