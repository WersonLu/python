#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/16 15:09
 
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
assert u"百度" in driver.title

elem = driver.find_element_by_name("wd")
elem.clear()
elem.send_keys(u"搞基")
elem.send_keys(Keys.RETURN)
time.sleep(3)
assert u"搞基" not in driver.page_source
driver.close()
