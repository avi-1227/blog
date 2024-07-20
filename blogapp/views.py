from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.all().filter(status=Post.Status.PUBLISHED)
    return render(request, 'blogapp/post/list.html', {'posts':posts})


def post_detail(request, id, post):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED, slug=post)
    return render(request, 'blogapp/post/detail.html', {'post':post})