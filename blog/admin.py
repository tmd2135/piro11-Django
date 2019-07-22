from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post,Comment
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','content_size', 'status','created_at','updated_at']

    actions = ['make_draft','make_published']

    def content_size(self,post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))
    content_size.short_description = '글자수'

    def make_draft(self,request,queryset):
        update_count = queryset.update(status='p')
        self.message_user(request,'{}건의 포스팅을 Draft상태로 변경'.format(update_count))
    make_draft.short_description = '지정 포스팅을 Draft상태로 변경'

    def make_published(self,request,queryset):
        update_count = queryset.update(status='p')
        self.message_user(request,'{}건의 포스팅을 Published상태로 변경'.format(update_count))
    make_published.short_description = '지정 포스팅을 Published상태로 변경'
#admin에 Post를 등록
#한번만 등록
# admin.site.register(Post)
#기본유저를 바꾸고싶을때 해지하고 등록할때 사용
# admin.site.unregister(Post)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


