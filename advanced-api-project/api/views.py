# api/views.py

from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

class BookListAPIView(generics.ListAPIView):
    """
    A view to list all books. Read-only access is allowed for all users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookDetailAPIView(generics.RetrieveAPIView):
    """
    A view to retrieve a single book. Read-only access for all users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookCreateAPIView(generics.CreateAPIView):
    """
    A view to create a new book. Only authenticated users can perform this action.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookUpdateAPIView(generics.UpdateAPIView):
    """
    A view to update an existing book. Only authenticated users can perform this action.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookDeleteAPIView(generics.DestroyAPIView):
    """
    A view to delete an existing book. Only authenticated users can perform this action.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
