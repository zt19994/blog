#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from django.contrib import admin
from .models import Category, Tag, Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    """ 可以在后台Post中显示指定信息"""
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)