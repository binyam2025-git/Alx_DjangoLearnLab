# api/views.py

from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions for a Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Configure permissions for different actions
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]
    
    # Add filtering, searching, and ordering for list views
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name']
    filterset_fields = ['title', 'author', 'publication_year']
    ordering_fields = ['publication_year', 'title']
    
    def get_queryset(self):
        """
        Optionally restricts the returned books by publication year.
        """
        queryset = super().get_queryset()
        publication_year = self.request.query_params.get('publication_year')
        if publication_year:
            queryset = queryset.filter(publication_year=publication_year)
        return queryset