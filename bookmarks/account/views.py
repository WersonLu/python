from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required


def user_login(request):
    # 当
    # user_login
    # 被一个
    # GET
    # 请求（request）调
    # 用，我们实例化一个新的登录表单（form）并通过
    # form = LoginForm()
    # 在模板（template）中展示它
    if request.method == 'POST':
        form = LoginForm(request.POST)
        #
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('登录成功')
                else:
                    return HttpResponse('登录失败')
            else:
                return HttpResponse('已经登录')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required()
def dashboard(request):
    render(request, 'account/dashboard.html',
           {'section': dashboard})
