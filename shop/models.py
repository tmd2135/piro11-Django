from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
    #related_name ='+' related_name을 쓰지 않겠다는 것 (중복방지)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='+')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)