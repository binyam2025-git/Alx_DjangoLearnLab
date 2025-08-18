
from accounts.models import CustomUser
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import CustomUserSerializer, TokenSerializer




# Get the active user model for consistent references
User = get_user_model()

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class RetrieveTokenView(APIView):
    def post(self, request):
        user = request.user
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    
class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(User, id=user_id)
        
        if request.user == user_to_follow:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(user_to_follow)
        return Response({'status': 'followed'}, status=status.HTTP_200_OK)

    def delete(self, request, user_id):
        user_to_unfollow = get_object_or_404(User, id=user_id)
        
        if request.user == user_to_unfollow:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.remove(user_to_unfollow)
        return Response({'status': 'unfollowed'}, status=status.HTTP_204_NO_CONTENT)

class ProfileView(generics.RetrieveAPIView):
    # Your profile view logic goes here.
    # You'll need to define queryset and serializer_class.
    pass