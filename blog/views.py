from django.core.paginator import Paginator
from django.shortcuts import render
from . import models

# Create your views here.

def list_posts(request):
    post_list = models.Post.objects.all()
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/list_posts.html', {
        'posts': posts,
    })

def post_detail(request, pk):
    return render(request, 'blog/post_detail.html', {
        'post': models.Post.objects.get(pk=pk),
    })
