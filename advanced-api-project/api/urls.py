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
    # URL for retrieving a list of all books and creating a new one
    path('books/', BookListView.as_view(), name='book-list'),

    # URL for creating a new book (separate endpoint for clarity)
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # URL for retrieving a single book
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    
    # URL for updating a specific book
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    
    # URL for deleting a specific book
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]