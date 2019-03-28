import xadmin

from .models import *

class PostAdmin(object):
    #文章
    list_display = ['title','body','create_time','modify_time','author']
    search_fields = ['title','body','create_time','modify_time','author']
    list_filter = ['title','body','create_time','modify_time','author']
    style_fields = {"body": "ueditor"}


class TagAdmin(object):
    #标签
    list_display = ['name',]
    search_fields = ['name',]
    list_filter = ['name',]


class CategoryAdmin(object):
    #分类
    list_display = ['name',]
    search_fields = ['name',]
    list_filter = ['name',]




#将xadmin管理器与对应model进行关联
xadmin.site.register(Post,PostAdmin)
xadmin.site.register(Tag,TagAdmin)
xadmin.site.register(Category,CategoryAdmin)

