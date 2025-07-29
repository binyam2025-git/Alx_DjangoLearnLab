# ~/Alx_DjangoLearnLab/api_project/api/serializers.py

from rest_framework import serializers
from .models import Book # Import your Book model

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__' # As per task, include all fields
        # Alternatively, specify fields explicitly:
        # fields = ['id', 'title', 'author', 'published_date', 'isbn']
        # (Use 'id' if you want the primary key in the JSON response)