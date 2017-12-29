#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/21 16:23
 
'''
import requests
import re
import datetime
import pymysql
import csv
import QRLogin


def parse_mood(i):
    text = re.sub('"commentlist":.*?"conlist":', '', i)
    if text:
        myMood = {}
        myMood["isTransfered"] = False

        tid = re.findall('"t1_termtype":.*?"tid":"(.*?)"', text)[0]  # 获取说说ID

        tid = qq + '_' + tid

        myMood['id'] = tid
        myMood['pos_y'] = 0
        myMood['pos_x'] = 0
        mood_cont = re.findall('\],"content":"(.*?)"', text)

        if re.findall('},"name":"(.*?)",', text):
            name = re.findall('},"name":"(.*?)",', text)[0]
            myMood['name'] = name
        if len(mood_cont) == 2:  # 如果长度为2则判断为属于转载
            myMood["Mood_cont"] = "评语:" + mood_cont[0] + "--------->转载内容:" + mood_cont[1]  # 说说内容
            myMood["isTransfered"] = True
        elif len(mood_cont) == 1:
            myMood["Mood_cont"] = mood_cont[0]
        else:
            myMood["Mood_cont"] = ""
        if re.findall('"created_time":(\d+)', text):
            created_time = re.findall('"created_time":(\d+)', text)[0]
            temp_pubTime = datetime.datetime.fromtimestamp(int(created_time))
            temp_pubTime = temp_pubTime.strftime("%Y-%m-%d %H:%M:%S")
            dt = temp_pubTime.split(' ')
            time = dt[1]
            myMood['time'] = time
            date = dt[0]
            myMood['date'] = date
        if re.findall('"source_name":"(.*?)"', text):
            source_name = re.findall('"source_name":"(.*?)"', text)[0]  # 获取发表的工具（如某手机）
            myMood['tool'] = source_name
        if re.findall('"pos_x":"(.*?)"', text):
            pos_x = re.findall('"pos_x":"(.*?)"', text)[0]
            pos_y = re.findall('"pos_y":"(.*?)"', text)[0]
            if pos_x:
                myMood['pos_x'] = pos_x
            if pos_y:
                myMood['pos_y'] = pos_y
            idname = re.findall('"idname":"(.*?)"', text)[0]
            myMood['idneme'] = idname
            cmtnum = re.findall('"cmtnum":(.*?),', text)[0]
            myMood['cmtnum'] = cmtnum
        return myMood


csv_reader = csv.reader(open('QQmail.csv'))
friend = []
for row in csv_reader:
    friend.append(row[1])
friend.pop(0)
# friends = []
# for f in friend:
#     f = f[:-7]
#     friends.append(f)
headers = {
    'Host': 'h5.qzone.qq.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://user.qzone.qq.com/790178228?_t_=0.22746974226377736',
    'Connection': 'keep-alive'
}  # 伪造浏览器头
conn = pymysql.connect(host='127.0.0.1',
                       user='root',
                       password='root',
                       port=3306,
                       db='51job',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()
cookie, gtk, qzonetoken = QRLogin.QR_login()
# requests 初始化
s = requests.session()
for qq in friend:
    for p in range(0, 1000):
        pos = p * 20
        params = {
            'uin': qq,
            'ftype': '0',
            'sort': '0',
            'pos': pos,
            'num': '20',
            'replynum': '100',
            'g_tk': gtk,
            'callback': '_preloadCallback',
            'code_version': '1',
            'format': 'jsonp',
            'need_private_comment': '1',
            'qzonetoken': qzonetoken
        }
        response = s.request('GET',
                             'https://h5.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6',
                             params=params, headers=headers, cookies=cookie)
        print(response.status_code)
        text = response.text

        if not re.search('lib', 'text'):
            print('%s说说下载完成' % qq)
            break
        textlist = re.split('\{"certified"', text)[1:]
        for i in textlist:
            data = {
                "id": myMood['id'],
                'time': myMood['time'],
                'content': myMood['Mood_cont']
            }
            print(data)
            myMood = parse_mood(i)
            try:
                insert_sql = '''
                                       insert into mood(id,content,time,sitename,pox_x,pox_y,tool,comments_num,date,isTransfered,name)
                                       VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                                    '''
                cursor.execute(insert_sql, (
                    myMood['id'], myMood["Mood_cont"], myMood['time'], myMood['idneme'], myMood['pos_x'],
                    myMood['pos_y'],
                    myMood['tool'], myMood['cmtnum'], myMood['date'], myMood["isTransfered"], myMood['name']))
                conn.commit()
            except:
                pass
print('说说下载完成')
