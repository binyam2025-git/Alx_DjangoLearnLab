# api/urls.py
from django.urls import path
from .views import BookListCreate, BookDetailUpdateDelete

urlpatterns = [
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailUpdateDelete.as_view(), name='book-detail-update-delete'),
]