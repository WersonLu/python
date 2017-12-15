#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/11 10:12
 
'''


class QQperson:
    def __init__(self,
                 Nickname,
                 Name,
                 Phone,
                 Mobile,
                 PagerHome,
                 HomePhone,
                 QQ,
                 BQQ,
                 Email):
        self.Nickname = Nickname
        self.Name = Name
        self.Phone = Phone
        self.Mobile = Mobile
        self.PagerHome = PagerHome
        self.HomePhone = HomePhone
        self.Phone = Phone
        self.QQ = QQ
        self.BQQ = BQQ
        self.Email = Email

    def sendsms(self):
        pass

    def senmail(self):
        pass

    def phonecall(self):
        pass
