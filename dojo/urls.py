from django.urls import re_path , path
from . import views
app_name = 'dojo'
urlpatterns = [
    re_path(r'^sum/(?P<numbers>[\d/]+)/$',views.mysum),
    re_path(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)$',views.hello),
    path('new/',views.post_new),
    re_path(r'^(?P<id>\d+)/edit/$',views.post_edit),
]