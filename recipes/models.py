#from django.db import models
# Alx_DjangoLearnLab/recipes/models.py
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField(help_text="List ingredients, one per line or comma separated")
    cooking_time_minutes = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(
        Category,
        related_name='recipes',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    owner = models.ForeignKey(
        User,
        related_name='recipes',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.title
