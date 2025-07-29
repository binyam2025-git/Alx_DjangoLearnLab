# bookshelf/serializers.py
from rest_framework import serializers
from .models import Book, Author # Import your Book model
import datetime # For calculating days since creation

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    # Custom field: Displays the number of days since the book was published
    # Assuming 'published_date' is the field for publication date.
    # If your field is 'publication_date', adjust the source attribute.
    #author = serializers.StringRelatedField()
    days_since_published = serializers.SerializerMethodField()
    author = AuthorSerializer()

    class Meta:
        model = Book
        # fields = '__all__' # Includes all model fields automatically
        # Or explicitly list fields, including your custom field
        fields = ['id', 'title', 'author', 'published_date', 'isbn', 'added_by', 'days_since_published']
        # Make sure 'isbn' and 'added_by' are actual fields in your Book model.
        # Adjust 'fields' list to match your actual Book model fields.

    def get_days_since_published(self, obj):

        if obj.published_date:
            return (datetime.date.today() - obj.published_date).days
        return None # Or 0, depending on desired behavior