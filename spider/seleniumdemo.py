#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/8 17:12
 
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")  # 通过驱动打开谷歌浏览器打开百度首页

assert u"百度" in driver.title
cookie={'name':'foo','value':'bar'}
driver.add_cookie(cookie)
driver.get_cookie()
elem = driver.find_element_by_name("wd")  # 通过类名找到搜索框
elem.clear()
elem.send_keys(u"网络爬虫")
elem.send_keys(Keys.RETURN)
time.sleep(3)
assert u"网络爬虫" not in driver.page_source
driver.close()

