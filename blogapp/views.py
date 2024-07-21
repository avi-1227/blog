from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
from django.views.decorators.http import require_POST

# Create your views here.

def post_list(request):
    posts = Post.objects.all().filter(status=Post.Status.PUBLISHED)
    return render(request, 'blogapp/post/list.html', {'posts':posts})


def post_detail(request, id, post):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED, slug=post)
    return render(request, 'blogapp/post/detail.html', {'post':post})


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post.post_url}\n\n {cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blogapp/post/share.html', {'post':post, 'form':form, 'sent':sent})


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    # A comment was posted
    form = CommentForm(data=request.POST)
    if form.is_valid():
        # Create a comment object without saving it to the database
        comment = form.save(commit=False)
        # Assign the post to the comment
        comment.post = post
        # Save the comment to the database
        comment.save()
    
    return render(request, 'blogapp/post/comment.html',{'post':post, 'form':form, 'comment':comment})