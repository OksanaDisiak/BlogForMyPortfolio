from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.mixins import ListModelMixin

from .models import MyPost
from .forms import CommentForm

# Create your views here.
from .serializers import MyPostSerializer


def home(request):
    posts = MyPost.objects
    return render(request, 'blogApp/home.html', {'posts': posts})


def show_post(request, post_id):
    post = get_object_or_404(MyPost, pk=post_id)
    return render(request, 'blogApp/post.html', {'post': post})


def comment(request, post_id):
    post = get_object_or_404(MyPost, pk=post_id)
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


class MyPostView(ListModelMixin, GenericAPIView):
    queryset = MyPost.objects.all()
    serializer_class = MyPostSerializer

    def get(self, *args, **kwargs):
        return self.list(*args, **kwargs)


class SingleMyPostView(RetrieveAPIView):
    queryset = MyPost.objects.all()
    serializer_class = MyPostSerializer


