from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='제목')    # 길이 제한 o
    content = models.TextField(verbose_name='내용')                # 길이 제한 x
    created_at = models.DateTimeField(auto_now_add=True)    #auto_now_add : 최초 저장할시 일시 저장
    updated_at = models.DateTimeField(auto_now=True)        #auto_now : 갱신이 될 때 마다 저장
