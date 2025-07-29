#from django.shortcuts import render
# Alx_DjangoLearnLab/recipes/views.py
from rest_framework import viewsets, permissions
from .models import Category, Recipe
from .serializers import CategorySerializer, RecipeSerializer
from django_filters.rest_framework import DjangoFilterBackend # Import filter backend
from rest_framework.filters import SearchFilter, OrderingFilter # Import search and ordering filters
from .permissions import IsOwnerOrReadOnly
import logging # <--- MAKE SURE THIS IS PRESENT

# Get an instance of a logger for this module
logger = logging.getLogger(__name__) # <--- ADD THIS LINE HERE



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
        # Log before saving
        logger.info(f"Attempting to create recipe by user: {self.request.user.username}")
        serializer.save(owner=self.request.user)
        # Log after saving
        logger.info(f"Recipe '{serializer.instance.title}' created by {self.request.user.username}")

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        logger.warning(f"User {request.user.username} is attempting to delete recipe: {instance.title} (ID: {instance.id})")
        return super().destroy(request, *args, **kwargs)