from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class Profile(models.Model):
    #OnetoOne 일시에는 setting.AUTH_USER_MODEL로 쓰는게 좋다
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)      #나쁜 케이스임 !!
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
