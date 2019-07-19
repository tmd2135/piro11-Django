import re
from django.db import models
from django.forms import ValidationError
def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*),value'):
        raise ValidationError('Invalid LngLat Type')

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('d','Draft'),
        ('p','Published')
    )
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100, verbose_name='제목')    # 길이 제한 o
    content = models.TextField(verbose_name='내용')                # 길이 제한 x
    tags= models.CharField(max_length=100,blank=True)
    lnglat = models.CharField(max_length=50,blank=True,
                help_text='위도/경도 포맷으로 입력',
                validators=[lnglat_validator])
    status= models.CharField(max_length=1,choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)    #auto_now_add : 최초 저장할시 일시 저장
    updated_at = models.DateTimeField(auto_now=True)        #auto_now : 갱신이 될 때 마다 저장
