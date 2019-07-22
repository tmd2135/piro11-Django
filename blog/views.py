from django.shortcuts import render
from .models import Post
# Create your views here.
def post_list(request):
    qs = Post.objects.all()     #전체 Post를 가져오는 qs
    return render(request,'blog/post_list.html',{
        'post_list': qs,
    })

