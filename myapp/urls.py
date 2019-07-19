from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^list1/$',views.post_list1),
    re_path(r'^list2/$',views.post_list2),
    re_path(r'^list3/$', views.post_list3),
    # re_path(r'^excel/$', views.excel_download()),
]