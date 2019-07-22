from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.post_list),
    re_path(r'^(?P<id>\d+)/$',views.post_detail),
]