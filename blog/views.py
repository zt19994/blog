#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """ 
        建立首页的视图函数，要与urls相对应
        使用render来渲染网页；
        
    """
    return render(request, 'blog/index.html', context={
        'title': '我的博客首页',
        'welcome': '欢迎来到我的博客首页',
    })