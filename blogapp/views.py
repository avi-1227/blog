from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import EmailPostForm

# Create your views here.

def post_list(request):
    posts = Post.objects.all().filter(status=Post.Status.PUBLISHED)
    return render(request, 'blogapp/post/list.html', {'posts':posts})


def post_detail(request, id, post):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED, slug=post)
    return render(request, 'blogapp/post/detail.html', {'post':post})


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
    else:
        form = EmailPostForm()
    return render(request, 'blogapp/post/share.html', {'post':post, 'form':form})