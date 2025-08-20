from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Like, Comment  # Ensure Comment is imported
from .serializers import PostSerializer, CommentSerializer  # Ensure CommentSerializer is imported

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get the current user
        user = self.request.user
        # Get the list of users the current user is following
        following_users = user.following.all()  # Adjust this if following is a ManyToMany field
        # Filter posts by those users
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

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