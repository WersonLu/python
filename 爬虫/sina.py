#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/29 15:29
 
'''
import time
import re
import os
import sys
import codecs
import shutil
import urllib
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
# driver = webdriver.PhantomJS(executable_path="D:\Anaconda3\Scripts\phantomjs.exe")
wait = ui.WebDriverWait(driver, 10)


# inforead = codecs.open("sinaweibo_list.txt", 'r', 'utf-8')
# infofile = codecs.open("sinaweibo_info.txt", 'a', 'utf-8')


def LoginWeibo(username, password):
    try:
        driver.get("https://passport.weibo.cn/signin/welcome")
        elem_btn = driver.find_element_by_css_selector("body > div > div > a.btn.btnWhite")
        elem_btn.click()
        elem_name = driver.find_element_by_xpath('//*[@id="loginName"]')
        elem_name.clear()
        elem_name.send_keys(username)  # 用户名
        elem_pwd = driver.find_element_by_xpath('//*[@id="loginPassword"]')
        elem_pwd.clear()
        elem_pwd.send_keys(password)  # 密码
        time.sleep(10)
        elem_sub = driver.find_element_by_id("loginAction")
        elem_sub.click()  # 点击登陆
        time.sleep(2)
        print(driver.current_url)
        print(driver.get_cookies())
        for cookie in driver.get_cookies():
            for key in cookie:
                print(key, cookie[key])
        print("登录成功")
    except Exception as e:
        print(e)
    finally:
        print(u'登录结束\n\n')


if __name__ == '__main__':
    username = '13249841723'
    password = 'wbcnm123456'
    LoginWeibo(username, password)
