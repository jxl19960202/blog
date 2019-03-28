from django.db import models
from django.contrib.auth.models import User    #django系统自带用户表
from DjangoUeditor.models import UEditorField

# Create your models here.

class Category(models.Model):
    '''
    标题分类
    '''
    name = models.CharField(max_length=50)
    class Meta:
        verbose_name='分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    '''
    标签
    '''
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Post(models.Model):
    '''
    文章
    '''
    title = models.CharField(max_length=50,verbose_name='标题')
    # body = models.TextField(verbose_name='主体')

    #富文本编辑内容:
    body = UEditorField(verbose_name='课程详情', width=600, height=300, toolbars="full", imagePath="blog/ueditor/",
                          filePath="blog/ueditor/", upload_settings={"imageMaxSize": 1204000}, default='')

    create_time = models.DateTimeField(verbose_name='创建时间')
    modify_time = models.DateTimeField(verbose_name='修改时间')
    excerpt = models.CharField(max_length=200, blank=True,verbose_name='摘要')  #blank=True 可以为空
    category = models.ForeignKey(Category,on_delete='CASCADE',verbose_name='分类')
    tags = models.ManyToManyField(Tag, blank=True,verbose_name='标签')  #ManyToManyField,多对多
    author = models.ForeignKey(User,verbose_name='作者',blank=True,on_delete='CASCADE')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title









































