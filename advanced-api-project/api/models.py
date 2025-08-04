# api/models.py
from django.db import models

class Author(models.Model):
    """Model representing an author."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Model representing a book, linked to an Author.
    This establishes a one-to-many relationship (one author can have many books).
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} by {self.author.name}"
