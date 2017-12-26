#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/23 7:17
 
'''
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests
import json


def to_write(content_dict):
    f.writelines('回帖时间：' + str(content_dict['topic_reply_time']) + '\n')
    f.writelines('回帖内容：' + str(content_dict['topic_reply_content']) + '\n')
    f.writelines('回帖作者：' + str(content_dict['user_name']) + '\n\n')


def spider(url):
    html = requests.get(url)
    selector = etree.HTML(html.content)
    content_filed = selector.xpath('//div[@class="l_post j_l_post l_post_bright  "]')
    item = {}
    for each in content_filed:
        reply_info = json.loads(each.xpath('@data-field')[0].replace('&quot', ''))
        author = reply_info['author']['user_name']
        content = each.xpath('.//cc/div/text()')[0].strip()
        reply_time = reply_info['content']['date']

        print(author)
        item['user_name'] = author
        item['topic_reply_content'] = content
        item['topic_reply_time'] = reply_time
        to_write(item)


if __name__ == "__main__":
    pool = ThreadPool(4)
    f = open('tieba.txt', 'w', encoding='utf-8')
    page = []
    for i in range(1, 600):
        newpage = 'http://tieba.baidu.com/p/3522395718?pn=' + str(i)
        page.append(newpage)
    result = pool.map(spider, page)
    pool.close()
    pool.join()
    f.close()
