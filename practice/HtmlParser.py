#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/7 14:44
 
'''
# html解析器
import re
import urllib
from bs4 import BeautifulSoup


class HtmlParse(object):
    # 方法的参数为下载页url,下载页内容cont,
    def parser(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()

        links = soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))

        for link in links:
            new_url = link['href']
            new_full_url = urllib.urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        data = {}
        data['url'] = page_url
        title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title'] = title.get_text()
        sumary = soup.find('div', class_='lemma-summary')
        data['sunmmary'] = sumary.get_text()
        return data
