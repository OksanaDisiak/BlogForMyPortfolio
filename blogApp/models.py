from django.db import models
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def get_summary(self):
        return self.text[:70]

    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    commentator = models.CharField(max_length=50)
    text = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.commentator + "'s comment to post " + self.post.title

    def approve(self):
        self.approved_comment = True
        self.save()