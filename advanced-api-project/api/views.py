# api/views.py

from rest_framework import generics, permissions, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book, Author
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    A view to list all books with filtering, searching, and ordering.
    Read-only access is allowed for all users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Add these lines to enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Configure fields for filtering
    filterset_fields = ['title', 'author', 'publication_year']
    
    # Configure fields for searching.
    # The '__name' lookup allows searching by the author's name, not just their ID.
    search_fields = ['title', 'author__name']
    
    # Configure fields for ordering
    ordering_fields = ['publication_year', 'title']

class BookDetailView(generics.RetrieveAPIView):
    """
    A view to retrieve a single book.
    Read-only access is allowed for all users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    """
    A view to create a new book.
    Only authenticated users can perform this action.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    """
    A view to update an existing book.
    Only authenticated users can perform this action.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """
    A view to delete an existing book.
    Only authenticated users can perform this action.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]