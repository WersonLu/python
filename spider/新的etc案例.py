#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ssl
from selenium import webdriver
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib


# 集思录爬虫类


class JSL:
    # 初始化变量
    # 传入url
    # 传入filename文件名
    # 传入is_ssl的值,1为使用ssl认证,0为禁用ssl认证
    # 传入single_line的值,1为获取单行数据,2为获取双行数据,默认为0获取所有数据
    # 传入increase_threshold的值,默认为1.00,即涨幅超过1%就发送通知

    def __init__(self, url, filename, increase_threshold=1.00):
        # 爬虫的url
        self.url = url
        # 保存内容的文件名
        self.filename = filename
        # 设置是否启用ssl
        # self.ssl = is_ssl
        # 设置获取哪些行
        # self.single_line = single_line
        # 设置通知的涨幅阈值
        self.increase_threshold = increase_threshold
        # 定义xpath
        self.xpath = '/html/body/div[3]/div[1]/div[1]/table/tbody/tr'
        # Email地址和口令:
        self.from_addr = 'wersonlau@163.com'
        self.password = 'wycnm123'
        # SMTP服务器地址:
        self.smtp_server = 'smtp.163.com'
        # 收件人地址:
        self.to_addr = '1066493443@qq.com'
        # 调用setSsl方法
        # self.setSsl()

        # 定义ssl方法

    # def setSsl(self):
    #     if self.ssl == 0:
    #         ssl._create_default_https_context = ssl._create_unverified_context()
    #     elif self.ssl == 1:
    #         pass
    #     else:
    #         return None

            # 设置浏览器驱动方法

    def setWebdrive(self):
        browser = webdriver.PhantomJS()
        return browser

        # 传入浏览器驱动和url,返回网页源码

    def getPageSource(self, browser, url):
        # page = browser.get(url)
        browser.get(url)
        browser.implicitly_wait(3)
        return browser
        print('获取到了?')

        # 传入网页源码，获取匹配的内容，然后写入contents并返回

    def getContent(self, browser):
        contents = []  # 定义list,用于存储匹配的数据
        for tr in browser.find_elements_by_xpath(self.xpath):
            content = tr.text.encode('utf-8')
            contents.append(content)
        return contents

        # 传入获取匹配的内容，把所需数据写入文件的方法

    def writeData(self, contents):
        file = open(self.filename, 'a+')
        # if self.single_line == 1:
        #     for index, content in enumerate(contents):
        #         if index % 2 == 0:
        #             file.write(content + '\n')
        # elif self.single_line == 2:
        #     for index, content in enumerate(contents):
        #         if index % 2 == 1:
        #             file.write(content + '\n')
        # else:
        for content in contents:
            file.write(content + '\n')
        file.close()

        # 发送邮件方法

    def sendEmail(self, notice_contents):
        # 函数_format_addr()用来格式化一个邮件地址
        def _format_addr(s):
            name, addr = parseaddr(s)
            return formataddr((
                Header(name, 'utf-8').encode(),
                addr if isinstance(addr, str) else addr))
            # Email地址和口令:

        from_addr = self.from_addr
        password = self.password
        # SMTP服务器地址:
        smtp_server = self.smtp_server
        # 收件人地址:
        to_addr = self.to_addr
        # 构造邮件
        msgtext = "\n".join(notice_contents)
        msg = MIMEText(msgtext, 'plain', 'utf-8')
        msg['From'] = _format_addr('etf爬虫通知<%s>' % from_addr)
        msg['To'] = _format_addr('管理员<%s>' % to_addr)
        msg['Subject'] = Header('来自Spider_jisilu_4爬虫的通知...如下内容超过了预设涨幅阈值' + str(self.increase_threshold) + '%',
                                'utf-8').encode()

        server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
        # server.set_debuglevel(1)      #可以打印出和SMTP服务器交互的所有信息
        server.login(from_addr, password)  # 登录SMTP服务器
        server.sendmail(from_addr, to_addr, msg.as_string())  # 发邮件
        server.quit()

        # 判断是否超过预设阈值方法

    def judgmentIncrease(self, contents):
        notice_contents = []  # 定义list,用于存储大于预设阈值的数据
        for i, line in enumerate(contents):
            a = float(line.split()[3][:-1])  # 取取出百分号的数字,并转成float类型
            if a > self.increase_threshold:  # 判断涨幅是否大于预设阈值
                notice_content = str(line.split()[1]) + ' 涨跌幅超过 ' + str(self.increase_threshold) + '%' + ' 涨跌幅为' + \
                                 str(line.split()[3]) + "\n"
                notice_contents.append(notice_content)
        return notice_contents

        # 开始方法

    def start(self):
        browser = self.setWebdrive()
        page = self.getPageSource(browser, self.url)
        contents = self.getContent(page)
        if not contents:
            print("获取内容失败,请确认URL是否正确")

            return
        else:
            notice_contents = self.judgmentIncrease(contents)
            if notice_contents:
                # self.sendEmail(notice_contents)
                print("已发送邮件通知，请查收！")

            self.writeData(contents)
            print("内容已写入" + self.filename)

        # 实例化对象jsl


# 传入url
# 传入filename文件名
# 传入is_ssl的值,1为使用ssl认证,0为禁用ssl认证
# 传入single_line的值,1为获取单行数据,2为获取双行数据,默认为0获取所有数据
# (url, filename, is_ssl, single_line=0, increase_threshold=1.00)
jsl = JSL("https://www.jisilu.cn/data/cbnew/#tlink_3",
          '07150214-2.txt', 0.3)
# jsl = JSL("https://www.jisilu.cn/data/cf/#stock",'kkk2.txt', 0, 0)
# jsl = JSL("https://www.jisilu.cn/data/sfnew/#tlink_3",'kkk2.txt', 0, 0)   #更改xpath为//*[@id="flex3"]/tbody/tr
# 调用start方法
jsl.start()
