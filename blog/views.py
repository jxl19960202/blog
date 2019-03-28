from django.shortcuts import render,HttpResponseRedirect,reverse
from django.views.generic.base import View  #类视图函数
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger   #分页
import markdown

from .models import Post,Category,Tag
from comments.forms import CommentForm
# Create your views here.

class IndexView(View):
    '''
    首页
    '''
    def get(self,request):
        #文章
        post_list = Post.objects.all()

        #分类
        Category_list = Category.objects.all()

        #标签
        tag_list = Tag.objects.all()

        # # ------------------分页----------------
        # try:
        #     page = request.GET.get('page', 1)
        # except PageNotAnInteger:
        #     page = 1
        #
        # # Paginator() 传入一个可迭代参数,一个数字(1页显示的元素个数)
        # p = Paginator(post_list, 1, request=request)
        # post_list = p.page(page)  #生成的是分页的对象
        # #在模板中for循环遍历,需要调用该对象的 object_list.
        # #  如:{% for course in all_course.object_list %}
        return render(request,'index.html',{
            'post_list':post_list,
            'Category_list':Category_list,
            'tag_list':tag_list
        })


class PostView(View):
    '''
    文章详情页
    '''
    def get(self,request,post_id):
        post = Post.objects.get(id=post_id)
        # 记得在顶部导入 CommentForm
        form = CommentForm()
        # 获取这篇 post 下的全部评论
        comment_list = post.comment_set.all()

        # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
        context = {'post': post,
                   'form': form,
                   'comment_list': comment_list
                   }
        return render(request, 'detail.html', context=context)




class CategoryView(View):
    '''
    标签页文章
    '''
    def get(self,request,category_id):
        #文章分类
        category= Category.objects.get(id=category_id)
        post_list = Post.objects.filter(category=category)

        # #分页
        # try:
        #     page = request.GET.get('page', 1)
        # except PageNotAnInteger:
        #     page = 1
        # p = Paginator(post_list, 1, request=request)
        # post_list = p.page(page)  #生成的是分页的对象
        # #在模板中for循环遍历,需要调用该对象的 object_list.
        return render(request,'archiveindex.html',{
            'port_list':post_list
        })


class ArchiveView(View):
    '''
    时间归档文章
    '''
    def get(self,request,year,month):
        #文章
        post_list = Post.objects.filter(create_time__year=int(year),
                                        create_time__month=int(month)
                                        ).order_by('-create_time')

        #分页
        # try:
        #     page = request.GET.get('page', 1)
        # except PageNotAnInteger:
        #     page = 1
        # p = Paginator(post_list, 1, request=request)
        # post_list = p.page(page)  #生成的是分页的对象
        # #在模板中for循环遍历,需要调用该对象的 object_list.
        return render(request,'index_time.html',{
            'port_list':post_list
        })
