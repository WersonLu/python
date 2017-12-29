#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/28 10:17
 
'''
from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # 文章详情页url配置
    url(r'^post/(?P<pk>[0-9]+)/$)', views.detail, name='detail')
]
