from django.shortcuts import render
from .models import Post
# Create your views here.
def post_list(request):
    qs = Post.objects.all()     #전체 Post를 가져오는 qs

    #q에 GET으로 가져와서 있으면 'q' 없으면 ''
    q = request.GET.get('q','')
    if q:
        qs = qs.filter(title__icontains=q)

    return render(request,'blog/post_list.html',{
        'post_list': qs,
        'q' : q,
    })

