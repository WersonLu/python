#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/11 11:10
 
'''
# 发送短信
import http.client
import urllib


class SendSms:

    def __init__(self, account, password):
        self.host = "106.ihuyi.com"
        self.sms_send_uri = "/webservice/sms.php?method=Submit"

        # 用户名是登录用户中心->验证码短信->产品总览->APIID
        self.account = account
        # 密码 查看密码请登录用户中心->验证码短信->产品总览->APIKEY
        self.password = password

    # 发送短信
    def send_sms(self, text, mobile):
        params = urllib.parse.urlencode(
            {'account': self.account, 'password': self.password, 'content': text, 'mobile': mobile, 'format': 'json'})
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        conn = http.client.HTTPConnection(self.host, port=80, timeout=30)
        conn.request("POST", self.sms_send_uri, params, headers)
        response = conn.getresponse()
        response_str = response.read()
        conn.close()
        return response_str

    # 批量发送
    def sen_smss(self, text, moblielist):
        for moblie in moblielist:
            print(self.send_sms(text, str(moblie)))


sender1 = SendSms("C72263836", "9c52e9f9dc3c3a3f8b89f4d593b577f9")
sender1.send_sms("您的验证码是:123546.不要说是我发的", "13428780135")
