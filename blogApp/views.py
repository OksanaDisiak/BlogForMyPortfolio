from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects
    return render(request, 'blogApp/home.html', {'posts': posts})


def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blogApp/post.html', {'post': post})