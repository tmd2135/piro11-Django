from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','content_size','created_at','updated_at']

    def content_size(self,post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))
    content_size.short_description = '글자수'

#admin에 Post를 등록
#한번만 등록
# admin.site.register(Post)
#기본유저를 바꾸고싶을때 해지하고 등록할때 사용
# admin.site.unregister(Post)

