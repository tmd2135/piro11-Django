from django.urls import path,re_path
from . import views_cbv
from . import views
app_name = 'blog'
urlpatterns = [
    path('',views.post_list, name='post_list'),
    re_path(r'^(?P<id>\d+)/$',views.post_detail,name='post_detail'),
    path('cbv/new/',views_cbv.post_new),
]