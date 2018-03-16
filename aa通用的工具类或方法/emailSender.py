#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
@File    : emailSender.py
'''
import smtplib
from email.mime.text import MIMEText


class EmailSender(object):
    def __init__(self):
        # 发送者的邮箱和授权码,服务器,接受者
        self.from_addr = 'wersonlau@163.com'
        self.password = '****'
        self.smtp_server = 'smtp.163.com'
        self.to_addr = '1066493443@qq.com'

    def send_mail(self, subject, body):
        """
        :param subject: 邮件标题
        :param body: 内容
        :return:
        """
        from_addr = self.from_addr
        password = self.password
        smtp_server = self.smtp_server
        to_addr = self.to_addr
        message = MIMEText(body, 'plain', 'utf-8')
        message['From'] = from_addr
        message['To'] = to_addr
        message['Subject'] = subject

        server = smtplib.SMTP(smtp_server, 25)
        try:
            server.login(from_addr, password)
            server.sendmail(from_addr, to_addr, message.as_string())
            server.quit()
            print("启动邮件发送成功了")
        except Exception as e:
            print("未知错误", e)

        # try:
        #     smtpSSLClient = smtplib.SMTP_SSL(self.smtp_host, self.smtp_port)  # 实例化一个SMTP_SSL对象
        #     loginRes = smtpSSLClient.login(self.smtp_user, self.smtp_pwd)  # 登录smtp服务器
        #     print(f"登录结果：loginRes = {loginRes}")
        #     if loginRes and loginRes[0] == 235:
        #         print(f"登录成功，code = {loginRes[0]}")
        #         smtpSSLClient.sendmail(self.sender, tolist, message.as_string())
        #         print(f"mail has been send successfully. message:{message.as_string()}")
        #     else:
        #         print(f"登陆失败，code = {loginRes[0]}")
        # except Exception as e:
        #     print(f"发送失败，Exception: e={e}")
