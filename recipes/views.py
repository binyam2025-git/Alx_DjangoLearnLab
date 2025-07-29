#from django.shortcuts import render
# Alx_DjangoLearnLab/recipes/views.py
from rest_framework import viewsets, permissions
from .models import Category, Recipe
from .serializers import CategorySerializer, RecipeSerializer
from django_filters.rest_framework import DjangoFilterBackend # Import filter backend
from rest_framework.filters import SearchFilter, OrderingFilter # Import search and ordering filters
from .permissions import IsOwnerOrReadOnly

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # Allow any user to read, but only authenticated users to create/update/delete
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name'] # Allow searching categories by name
    ordering_fields = ['name'] # Allow ordering categories by name

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    # Allow any user to read, but only authenticated users to create/update/delete
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'owner'] # Allow filtering recipes by category or owner ID
    search_fields = ['title', 'description', 'ingredients'] # Allow searching by title, description, ingredients
    ordering_fields = ['created_at', 'title', 'cooking_time_minutes'] # Allow ordering by these fields

    def perform_create(self, serializer):
        # When creating a recipe, automatically set the owner to the current user
        serializer.save(owner=self.request.user)