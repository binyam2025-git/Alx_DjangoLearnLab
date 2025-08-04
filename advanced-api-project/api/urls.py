# api/urls.py

from django.urls import path
from .views import (
    BookListView, 
    BookDetailView, 
    BookCreateView, 
    BookUpdateView, 
    BookDeleteView
)

urlpatterns = [
    # URL for retrieving a list of all books
    path('books/', BookListView.as_view(), name='book-list'),

    # URL for creating a new book
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # URL for retrieving, updating, or deleting a specific book
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]