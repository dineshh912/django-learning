# api/views.py
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
) 
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly
)
from blog.models import Post
from ..serializers.blog_serializers import BlogSerializers
from ..permissions import IsAuthorOrReadOnly
from rest_framework import viewsets

class BlogListAPIView(ListCreateAPIView):
    """
        Blog List API View
    """
    queryset = Post.objects.all()
    serializer_class = BlogSerializers


class BlogDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
        Blog Detail API View
    """
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = BlogSerializers


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = BlogSerializers