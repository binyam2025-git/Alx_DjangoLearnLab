from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from notifications.models import Notification
from .models import Post, Like
from rest_framework.views import APIView

User = get_user_model()

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            # Create a notification for the post's author
            if request.user != post.author:
                Notification.objects.create(
                    recipient=post.author,
                    actor=request.user,
                    verb="liked",
                    target=post
                )
            return Response({"detail": "Post liked."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "Post already liked."}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({"detail": "Post unliked."}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({"detail": "Post is not liked."}, status=status.HTTP_400_BAD_REQUEST)