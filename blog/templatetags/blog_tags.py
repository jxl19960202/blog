'''
用于存放自定义的模板语法
首先导入 template 这个模块，然后实例化了一个 template.Library 类，并将函数 get_recent_posts 装饰为
register.simple_tag。这样就可以在模板中使用语法 {% get_recent_posts %} 调用这个函数了。
'''

from django import template

from ..models import Post,Category,Tag


register = template.Library()

@register.simple_tag
def get_recent_ports(num=3):
    #最新的文章模板
    return Post.objects.all().order_by('-create_time')[:num]


@register.simple_tag
def archives():
    '''
    按照时间分类.归档
    这里 dates 方法会返回一个列表，列表中的元素为每一篇文章（Post）的创建时间，
    且是 Python 的 date 对象，精确到月份，降序排列。接受的三个参数值表明了这些含义，
    一个是 created_time ，即 Post 的创建时间，month 是精度，order='DESC' 表明降序排列
    （即离当前越近的时间越排在前面）。例如我们写了 3 篇文章，分别发布于 2017 年 2 月 21 日、2017 年 3 月 25 日、
    2017 年 3 月 28 日，那么 dates 函数将返回 2017 年 3 月 和 2017 年 2 月这样一个时间列表，且降序排列，从而帮助
    我们实现按月归档的目的。
    '''
    return Post.objects.dates('create_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    #分类模板
    return Category.objects.all()










