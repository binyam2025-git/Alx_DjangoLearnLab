from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Includes custom validation to ensure the publication year is not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Custom validation method for the publication_year field.
        Ensures the publication year is not a future year.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    This serializer demonstrates a nested relationship by including
    a list of all related books for a given author.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']