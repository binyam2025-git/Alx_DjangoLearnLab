from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token  # Import Token

class CustomUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)  # Ensure username is a CharField
    email = serializers.EmailField(required=True)     # Email field
    password = serializers.CharField(write_only=True)  # Password field

    class Meta:
        model = get_user_model()  # Use the custom user model
        fields = ['id', 'username', 'email', 'password']  # Add other fields as needed

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        
        # Create a token for the user
        Token.objects.create(user=user)
        
        return user