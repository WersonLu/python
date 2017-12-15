#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     zhihu
   Author :       aaa
   date：          2017/12/10
-------------------------------------------------
"""
import  re
import requests

def get_xsrf(session):
    index_url='http://www.zhihu.com'
    index_page=session.get(index_url,headers=headers)
    html=index_page.text
    pattern=r'name="_xsrf"value="(.*?)"'
    _xsrf=re.findall(pattern,html)

    return _xsrf
agent=
