#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/11 12:47
 
'''
import smtplib  # 发邮件
from email.mime.text import MIMEText  # 邮件文本


class SendMail:
    def __init__(self, SMTPsever, Sender, password):
        self.SMTPsever = SMTPsever  # 服务器
        self.Sender = Sender  # 发送邮件的地址
        self.password = password  # 密码
        self.mailsever = smtplib.SMTP(self.SMTPsever, 25)  # 邮件服务器25端口
        self.mailsever.login(self.Sender, self.password)  # 登陆

    def Send(self, Message, title, maillist):  # 发送邮件,要标题,内容,接受者
        msg = MIMEText(Message)  # 转化邮件文本
        msg["Subject"] = title  # 邮件标题
        msg["From"] = self.Sender  # 邮件发送者
        msg["To"] = "yincheng8848@163.com"  # 收件人

        self.mailsever.sendmail(self.Sender,
                                maillist,
                                msg.as_string())

    def exit(self):
        self.mailsever.quit()


# 初始化一个发送邮件类,带基本参数
sender1 = SendMail("smtp.163.com", "wersonliu@163.com", "wycnm123654")
# 类实例调用方法,带信息参数
sender1.Send("你好,面试邀请 ", "请先生在明天下午来面试，自带建立", ["wersonliu@163.com", "wersonliu@gmail.com"])
# 发送后关闭
sender1.exit()
