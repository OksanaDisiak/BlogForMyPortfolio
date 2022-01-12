from rest_framework import serializers
from .models import MyPost


class MyPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyPost
        fields = ('id', 'title', 'text', 'created_at', 'updated_at')
