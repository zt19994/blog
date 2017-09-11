#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" 
    创建一个app的urls
    并与视图绑定，url模板中，r'^$'为正则匹配，用来匹配网页
    view.index 是网页地址
    name='index' 指定视图中绑定的函数index
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]