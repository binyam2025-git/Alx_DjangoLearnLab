#from django.contrib import admin
# Alx_DjangoLearnLab/recipes/admin.py
from django.contrib import admin
from .models import Category, Recipe

admin.site.register(Category)
admin.site.register(Recipe)

