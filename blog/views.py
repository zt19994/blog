#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    """ 
        建立首页的视图函数，要与urls相对应
        使用render来渲染网页；
        导入Post，在首页显示文字列表；all()表示显示全部，order_by()函数是排序，
        在created_time前加-号，表示逆序，不加表示正序
        
    """
    # post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={
        'title': '我的博客首页',
        'welcome': '欢迎来到我的博客首页',

    })