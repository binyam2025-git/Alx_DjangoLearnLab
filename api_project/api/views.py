#from django.shortcuts import render

# ~/Alx_DjangoLearnLab/api_project/api/views.py

from rest_framework import generics # Import generics
from .models import Book         # Import your Book model
from .serializers import BookSerializer # Import your BookSerializer

class BookList(generics.ListAPIView): # Renamed to BookList as per task
    queryset = Book.objects.all()
    serializer_class = BookSerializer
