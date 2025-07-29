#from django.test import TestCase

# C:\Users\user\Alx_DjangoLearnLab\recipes\tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Category, Recipe

class RecipeAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.category = Category.objects.create(name='Test Category')
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            description='Test Description',
            ingredients='Test Ingredients',
            cooking_time_minutes=30,
            category=self.category,
            owner=self.user
        )

    def test_retrieve_recipes_list(self):
        """Ensure we can retrieve a list of recipes."""
        response = self.client.get(reverse('recipe-list')) # 'recipe-list' is the DRF default name
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1) # Check pagination results
        self.assertEqual(response.data['results'][0]['title'], 'Test Recipe')

    def test_create_recipe_authenticated(self):
        """Ensure we can create a recipe with authentication."""
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'New Recipe',
            'description': 'A new one',
            'ingredients': 'Some stuff',
            'cooking_time_minutes': 15,
            'category': self.category.id
        }
        # THIS LINE MUST BE PRESENT AND CORRECTLY INDENTED!
        response = self.client.post(reverse('recipe-list'), data, format='json')

        # --- DEBUG LINES (as previously provided) ---
        if response.status_code != status.HTTP_201_CREATED:
            print(f"\n--- DEBUG: Create Recipe Failed (Status: {response.status_code}) ---")
            print("Response Data:", response.data)
            print("--------------------------------------------------")
        # --- END DEBUG LINES ---

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Recipe.objects.count(), 2)

    def test_create_recipe_unauthenticated(self):
        """Ensure unauthenticated users cannot create a recipe."""
        data = {
            'title': 'Unauthorized Recipe',
            'description': 'A secret one',
            'ingredients': 'Secret stuff',
            'cooking_time_minutes': 5,
            'category': self.category.id
        }
        response = self.client.post(reverse('recipe-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED) # Or 403 Forbidden depending on DRF setting
