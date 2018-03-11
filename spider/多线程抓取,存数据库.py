#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
@File    : 多线程抓取,存数据库.py
'''
import requests
from bs4 import BeautifulSoup
import pymysql
import threading
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

"""
http://news.baidu.com
新闻标题、来源、发布日期
使用多线程爬取数据，每个线程爬取一个关键字的数据，并将爬取的数据写入到mysql数据库中。
（第一次爬取所有关键字对应的所有新闻，并写入数据库中，作为历史数据）定时每天每隔十分钟爬取每个关键字的第一页，
和数据库里的历史数据进行比较，如果有新数据则将新闻标题作为邮件内容发送。
title 
来源
发布日期
"""


# 邮件类
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


# # 初始化一个发送邮件类,带基本参数
# sender1 = SendMail("smtp.163.com", "wersonliu@163.com", 密码)
# # 类实例调用方法,带信息参数
# sender1.Send("你好,新消息 ", "xxxxx", ["wersonliu@163.com", "wersonliu@gmail.com"])
# # 发送后关闭
# sender1.exit()


# 存数据库
def save(title, from_url):
    db = pymysql.connect(host='localhost', user='root', password='root', database='news', port=3306)
    cur = db.cursor()
    sql_insert = """INSERT INTO baidunews(title,fromurl) VALUES(%s,%s,)"""
    """
    数据库这里需要查重处理,有新的新闻要实例邮件类发邮件
    """
    try:
        cur.execute(sql_insert, (title, from_url))
        db.commit()
        print('执行成功')
    except Exception as e:
        db.rollback()
    finally:
        db.close()



def get_page(keyword):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'}
    url = "http://news.baidu.com/ns?cl=2&rn=20&tn=news&word=" + keyword
    res = requests.get(url, headers=headers)
    res.encoding = 'UTF-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    for news in soup.select('.result'):
        h3 = news.select('h3')
        if len(h3) > 0:
            title = h3[0].text
            from_url = h3[0].select('a')[0]['href']
            news_time = news.select('.c-author')[0].text
            # "新华网  2018年03月06日 13:06" 这里对正则不太熟练,无法把两种格式的时间统转为一种标准的时间
            # "凤凰网  6小时前"  索性只去除空格
            rel_time = ''.join(news_time.split())
            print(title, from_url, rel_time)
            # save(title, from_url)


# 多线程
def many_thread():
    threads = []
    t1 = threading.Thread(target=get_page, args=('中国',))
    threads.append(t1)
    t2 = threading.Thread(target=get_page, args=('美国',))
    threads.append(t2)
    t3 = threading.Thread(target=get_page, args=('日本',))
    threads.append(t3)

    for t in threads:
        t.start()


if __name__ == '__main__':
    many_thread()

"""
面试临走之前问了下班时间,是五点半.由于之前答应了个公司明天报道(不想两边都搞砸了),而且网易邮箱把题目邮件归为垃圾分类了,
下午两点打电话问了才知道.毕竟没正式做过爬虫项目所以这个小题目,在三个小时内做的很仓促.数据库存储那边没做好.查了下资料,用scrapy可能更好.
之前用selenium 做过翻页爬取,现在一时没想到如何不用selenium时翻页爬取

"""