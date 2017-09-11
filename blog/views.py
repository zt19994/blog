#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """ 
        建立首页的视图函数，要与urls相对应
        并通过HttpResponse建立响应
    """
    return HttpResponse('<h1>这是博客首页</h1>')