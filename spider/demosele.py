#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/8 17:23
 
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")  # 通过驱动打开谷歌浏览器打开百度首页

cookie={'name':'foo','value':'bar'}
driver.add_cookie(cookie)
driver.get_cookie()