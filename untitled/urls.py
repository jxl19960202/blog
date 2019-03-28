"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.views.static import serve  #处理文件的视图

import xadmin
from django.urls import path,include,re_path
from untitled.settings import MEDIA_ROOT

from blog.views import IndexView

urlpatterns = [
    path('xadmin/', xadmin.site.urls),

    #首页
    path('', IndexView.as_view(), name='index'),

    #博客页面
    path('blog/',include('blog.urls',namespace='blog')),

    #博客评论
    path('comments/',include('comments.urls',namespace='comments')),

    # 配置富文本编辑url
    path('ueditor/', include('DjangoUeditor.urls')),

    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
]
