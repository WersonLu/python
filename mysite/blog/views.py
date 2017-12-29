from django.shortcuts import render
# 每一个视图都会接受一个http请求
# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html',
                  {'posts': posts})
