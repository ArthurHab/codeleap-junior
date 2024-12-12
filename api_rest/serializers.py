from rest_framework import serializers

from .models import Post

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['username','title','content']

class PostEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content']  

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'username','created_datatime', 'title','content']  