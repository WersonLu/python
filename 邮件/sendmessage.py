#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/11 10:40
 
'''
# 接口类型：互亿无线触发短信接口，支持发送验证码短信、订单通知短信等。
# 账户注册：请通过该地址开通账户http://sms.ihuyi.com/register.html
# 注意事项：
# （1）调试期间，请用默认的模板进行测试，默认模板详见接口文档；
# （2）请使用APIID（查看APIID请登录用户中心->验证码短信->产品总览->APIID）及 APIkey来调用接口；
# （3）该代码仅供接入互亿无线短信接口参考使用，客户可根据实际需要自行编写；

# !/usr/local/bin/python
# -*- coding:utf-8 -*-
import http.client
import urllib

host = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"

# 用户名是登录用户中心->验证码短信->产品总览->APIID
account = "C72263836"
# 密码 查看密码请登录用户中心->验证码短信->产品总览->APIKEY
password = "9c52e9f9dc3c3a3f8b89f4d593b577f9"


def send_sms(text, mobile):
    params = urllib.parse.urlencode(
        {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str


#
# if __name__ == '__main__':
#     mobile = "13164612960"
#     text = "您的验证码是：121254。请不要说是wersonliu发的。"
#     print(send_sms(text, mobile))
list = ["13164612960", "13249841723", "17386010627", "13428780135"]
text = "你的验证码是325647,请不要泄露"
for mob in list:
    print(mob)
    print(str(mob))
    print(send_sms(text, str(mob)))

# import json
# import requests
#
# class YunPian(object):
#     def __init__(self,api_key):
#         self.api_key=api_key
#         self.single_send_url="http://106.ihuyi.com/webservice/sms.php?method=Submit"
#
#     def send_sms(self,code,mobile):
#