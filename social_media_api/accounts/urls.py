# accounts/urls.py

#from .views import RegisterUserView, FollowView
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterUserView, LoginView, ProfileView, FollowUserView

urlpatterns = [
    #path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', FollowUserView.as_view(), name='unfollow_user'),
    path('register/', RegisterUserView.as_view(), name='register'),
]