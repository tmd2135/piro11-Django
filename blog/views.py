from django.http import Http404
from django.shortcuts import render, get_object_or_404
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

def post_detail(request,id):
    #예외처리
    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404
    post = get_object_or_404(Post,id=id)

    return render(request,'blog/post_detail.html',{
        'post': post,
    })