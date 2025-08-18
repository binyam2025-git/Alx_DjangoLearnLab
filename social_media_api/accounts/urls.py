# accounts/urls.py

from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, ProfileView, FollowView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'), # Note: Use obtain_auth_token for the provided login view
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', FollowView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', FollowView.as_view(), name='unfollow-user'),
]