from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:post_id>/comment/', views.comment, name='comment'),
    path('<int:post_id>/', views.post, name='post'),

    ]