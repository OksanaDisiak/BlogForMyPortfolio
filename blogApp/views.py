from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import CommentForm

# Create your views here.


def home(request):
    posts = Post.objects
    return render(request, 'blogApp/home.html', {'posts': posts})


def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blogApp/post.html', {'post': post})


def comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post', post_id=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blogApp/comment.html', {'form': form})



