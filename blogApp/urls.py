from django.urls import path
from . import views
from .views import MyPostView, SingleMyPostView

urlpatterns = [
    path('posts/', views.home, name='home'),
    path('posts/<int:post_id>/comment/', views.comment, name='comment'),
    path('posts/<int:post_id>/', views.show_post, name='post'),
    path('posts/', MyPostView.as_view()),
    path('posts/<int:pk>', SingleMyPostView.as_view()),

    ]
