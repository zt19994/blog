#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from django.contrib import admin
from .models import Category, Tag, Post

# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)