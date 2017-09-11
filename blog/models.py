from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    """ 
    分类，必须继承models.Model 
    name 使用CharField字符类型
    """
    name = models.CharField(max_length=100)


class Tag(models.Model):
    """
    标签：和category一样
    """
    name = models.CharField(max_length=100)


class Post(models.Model):
    """
    文章的数据结构包含多个内容；
    标题；
    正文；
    创建时间；
    最后修改时间；
    文章摘要；
    引入上面的分类和标签；
    作者；
    """

    # 文章标题，比较短，使用CharField字段
    title = models.CharField(max_length=50)

    # 正文内容,使用大文本字段TextField字段,正文比较多，不设置最大字数参数max_length
    body = models.TextField()

    # 摘要excerpt
    excerpt = models.CharField(max_length=100, blank=True)

    # 创建时间和最后修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 连接分类和标签
    # 文章分类是多对一  使用ForeignKey
    # 标签和文章是多对多 ManyToManyField
    # 参数black=True 表示允许空值
    category = models.ForeignKey(Category)
    tag = models.ManyToManyField(Tag, blank=True)

    # 作者和文章可以一对多
    author = models.ForeignKey(User)