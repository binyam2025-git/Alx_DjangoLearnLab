from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Like, Comment  # Ensure Comment is imported
from .serializers import PostSerializer, CommentSerializer  # Ensure CommentSerializer is imported

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.request.data['post'])
        serializer.save(author=self.request.user, post=post)

# Other views (like, unlike, etc.) can remain as they are or be adapted as needed.