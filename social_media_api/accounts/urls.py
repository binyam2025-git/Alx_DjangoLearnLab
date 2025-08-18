# accounts/urls.py

#from .views import RegisterUserView, FollowView
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterUserView, FollowUserView

urlpatterns = [
    #path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'), # Note: Use obtain_auth_token for the provided login view
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
    path('register/', RegisterUserView.as_view(), name='register'),
]