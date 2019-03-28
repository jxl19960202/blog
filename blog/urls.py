from django.urls import path,re_path,include


from .views import IndexView,PostView,CategoryView,ArchiveView


app_name = 'blog'
urlpatterns = [
    re_path('post/(?P<post_id>\d+)/',PostView.as_view(),name='post'),
    re_path(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', ArchiveView.as_view(), name='archives'),
    re_path('category/(?P<category_id>\d+)/',CategoryView.as_view(),name='category'),

]