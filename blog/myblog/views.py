from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


# 视图函数对应urls里的处理参数
def index(request):
    # return HttpResponse("myblog")
    return render(request, 'myblog/index.html', context={
        'title': '我的博客',
        'welcome': '欢迎光临'
    })

