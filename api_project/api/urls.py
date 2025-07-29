# ~/Alx_DjangoLearnLab/api_project/api/urls.py

from django.urls import path
from .views import BookList # Import your BookList view

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]