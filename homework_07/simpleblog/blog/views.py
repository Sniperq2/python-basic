from django.shortcuts import render
from django.utils import timezone

from .models import Post


def posts_list(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'post_list.html', {'posts': posts})


def index(request):
    return render(request, 'root.html', {})
