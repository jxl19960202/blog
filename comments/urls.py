from django.urls import path,include,re_path

from comments.views import PostCommentsView


app_name = 'comments'
urlpatterns = [
    re_path(r'^post/(?P<post_id>[0-9]+)/$', PostCommentsView.as_view(), name='post_comment'),
]