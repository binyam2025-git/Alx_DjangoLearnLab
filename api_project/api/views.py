# ~/Alx_DjangoLearnLab/api_project/api/views.py

# IMPORTANT: Change this import from `generics` to `viewsets`
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

# Replace the previous BookList class with BookViewSet
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
