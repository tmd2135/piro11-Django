import re
from django.db import models
from django.forms import ValidationError
from django.conf import settings

def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*),value'):
        raise ValidationError('Invalid LngLat Type')

# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = (
        ('d','Draft'),
        ('p','Published')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    # author = models.CharField(max_length=20)
    title = models.CharField(max_length=100, verbose_name='제목')    # 길이 제한 o
    content = models.TextField(verbose_name='내용')                # 길이 제한 x
    tags= models.CharField(max_length=100,blank=True)
    lnglat = models.CharField(max_length=50,blank=True,
                help_text='위도/경도 포맷으로 입력',
                validators=[lnglat_validator])
    status= models.CharField(max_length=1,choices=STATUS_CHOICES)
    #M:M 관계 (문자열로 클래스 지정)
    tag_set = models.ManyToManyField('Tag',blank=True)
    #
    created_at = models.DateTimeField(auto_now_add=True)    #auto_now_add : 최초 저장할시 일시 저장
    updated_at = models.DateTimeField(auto_now=True)        #auto_now : 갱신이 될 때 마다 저장



    class Meta:
        ordering = ['-id']      #해당 필드 내림차순 정렬
        # ordering = ['id']     #해당 필드 오름차순 정렬

    # return 값을 str로 변환
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name

