#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2018/2/18 9:11
 
'''
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.user_login, name='login')
]
