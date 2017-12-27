#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     urls
   Author :       aaa
   date：          2017/12/28
-------------------------------------------------
"""
from django.conf.urls import url

from . import views

urlpatterns = {
    url(r'^$', views.index, name='index')
}
