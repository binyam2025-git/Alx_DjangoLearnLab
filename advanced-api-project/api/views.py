# api/views.py

from rest_framework import generics, permissions, filters
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

class BookListView(generics.ListAPIView):
    """
    A view to list all books with filtering, searching, and ordering.
    Read-only access is allowed for all users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Add these lines to enable searching and ordering
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name']  # Search by book title or author name
    ordering_fields = ['publication_year', 'title'] # Order by publication year or title


