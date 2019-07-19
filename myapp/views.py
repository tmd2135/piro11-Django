import os
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
def post_list1(request):
    #FBV : 직접 문자열로 HTML형식 열기,
    name = '공유'
    return HttpResponse('''
<h1>AskDjango</h1>
<p>{name}</p>
<p>여러분의 파이썬&장고 페이스메이커가 되겠습니다.</p>'''.format(name=name))
def post_list2(request):
    #템플릿을 통해 HTML형식
    name = '공유'
    return render(request,'myapp/post_list.html',{'name':name})

def post_list3(request):
    return JsonResponse({
        'message': '안녕 파이썬&장고',
        'items': ['파이썬','장고','Celery','Azure','AWS'],
    },json_dumps_params={'ensure_ascii': False})


# def excel_download(request):
#     #'FBV: 엑셀 다운로드 응답하기'
#     filepath = '경로지정'
#     filename = os.path.basename(filepath)
#
#     with open(filepath, 'rb') as f:
#         response = HttpResponse(f, content_type='application/vnd.ms-excel')
#         # 필요한 응답헤더 세팅
#         response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
#         return response