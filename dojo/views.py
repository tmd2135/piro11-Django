from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from dojo.forms import PostForm
from .models import Post


def mysum(request,numbers):
    # numbers = "1233/12/2131242/123124215/12312/31/3
    result = sum(map(lambda s : int(s or 0),numbers.split("/")))
    return HttpResponse(result)

def hello(request,name,age):
    return HttpResponse('안녕하세요.{}.{}살이시네요.'.format(name,age))

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        #모든 값이 True 면 valid는 True
        if form.is_valid():
            # 밥ㅇ법 1
            # post = Post()
            # post.title = form.cleaned_data['title']
            # post.content = form.cleaned_data['content']
            # post.save()


            # 방법2
            # post = Post(title = form.cleaned_data['title'],
            #             content = form.cleaned_data['content'])
            # post.save()



            # 방법 3
            # post = Post.objects.create(title = form.cleaned_data['titlt'],
            #                            content = form.cleaned_data['content'])

            # 방법 4
            #중복 DB save를 방지
            post = form.save(commit=False)
            #사용자의 ip를 저장하는 방법
            post.ip = request.META['REMOTE_ADDR']
            post.save()

            print(form.cleaned_data)
            return redirect('/dojo/')

    else:
        form = PostForm()
    return render(request,'post_form.html',{
        'form' : form,
    })