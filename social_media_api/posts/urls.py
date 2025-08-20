from django.urls import path
from .views import PostListCreateView, PostDetailView, FeedView, LikePostView, UnlikePostView

urlpatterns = [
    path('', PostListCreateView.as_view(), name='post-list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('feed/', FeedView.as_view(), name='user_feed'),
    path('<int:pk>/like/', LikePostView.as_view(), name='like-post'), 
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'), 
]