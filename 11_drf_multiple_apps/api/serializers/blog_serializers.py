# api/serializers/blog_serializers.py

from rest_framework import serializers
from blog.models import Post


class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
