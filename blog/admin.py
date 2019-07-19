from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','created_at','updated_at']

#admin에 Post를 등록
#한번만 등록
# admin.site.register(Post)
#기본유저를 바꾸고싶을때 해지하고 등록할때 사용
# admin.site.unregister(Post)

