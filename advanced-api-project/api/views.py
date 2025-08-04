#from django.shortcuts import render
# api/views.py
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

class BookListCreate(generics.ListCreateAPIView):
    """
    A view to list all books or create a new book.
    - GET: Retrieves a list of all books.
    - POST: Creates a new book instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # This permission class allows read-only access to unauthenticated users,
    # but only authenticated users can create new books.

class BookDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    """
    A view to retrieve, update, or delete a single book instance.
    - GET: Retrieves a single book by its primary key (pk).
    - PUT: Updates an existing book.
    - PATCH: Partially updates an existing book.
    - DELETE: Deletes an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # Allows authenticated users to perform all actions,
    # and unauthenticated users to only perform read actions (GET).
