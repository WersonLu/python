#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2018/3/2 20:59
 
'''
import itchat
import re
import time
from itchat.content import *


@itchat.msg_register([TEXT, PICTURE, MAP, CARD, NOTE, SHARING, RECORDING, ATTACHMENT, VIDEO])
def text_reply(msg):
    if msg['Type'] == 'Text':
        reply_content = msg['Text']
    elif msg['Type'] == 'Picture':
        reply_content = r"图片: " + msg['FileName']
    elif msg['Type'] == 'Card':
        reply_content = r" " + msg['RecommendInfo']['NickName'] + r" 的名片"
    elif msg['Type'] == 'Map':
        x, y, location = re.search("<location x=\"(.*?)\" y=\"(.*?)\".*label=\"(.*?)\".*", msg['OriContent']).group(1,
                                                                                                                    2,
                                                                                                                    3)
        if location is None:
            reply_content = r"位置: 纬度->" + x.__str__() + " 经度->" + y.__str__()
        else:
            reply_content = r"位置: " + location
    elif msg['Type'] == 'Note':
        reply_content = r"通知"
    elif msg['Type'] == 'Sharing':
        reply_content = r"分享"
    elif msg['Type'] == 'Recording':
        reply_content = r"语音"
    elif msg['Type'] == 'Attachment':
        reply_content = r"文件: " + msg['FileName']
    elif msg['Type'] == 'Video':
        reply_content = r"视频: " + msg['FileName']
    else:
        reply_content = r"消息"

    friend = itchat.search_friends(userName=msg['FromUserName'])
    itchat.send(r"Friend:%s -- %s    "
                r"Time:%s    "
                r" Message:%s" % (friend['NickName'], friend['RemarkName'], time.ctime(), reply_content),
                toUserName='filehelper')

    itchat.send(r"我已经收到你在【%s】发送的消息【%s】稍后回复" % (time.ctime(), reply_content),
                toUserName=msg['filehelper'])


itchat.auto_login()
itchat.run()
