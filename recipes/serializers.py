# Alx_DjangoLearnLab/recipes/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User # For RecipeOwnerSerializer
from .models import Category, Recipe

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__' # Include all fields from the Category model

class RecipeOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username'] # Only expose id and username of the owner

class RecipeSerializer(serializers.ModelSerializer):
    # Nested serializer to display category details instead of just its ID
    category_detail = CategorySerializer(source='category', read_only=True)
    # Nested serializer for the owner
    owner_detail = RecipeOwnerSerializer(source='owner', read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'description', 'ingredients',
            'cooking_time_minutes', 'category', 'category_detail',
            'owner', 'owner_detail', 'created_at', 'updated_at'
        ]
        # Ensure 'owner' and 'category' are writeable (for POST/PUT)
        # but 'owner_detail' and 'category_detail' are read-only (for GET)
        read_only_fields = ['created_at', 'updated_at', 'owner']