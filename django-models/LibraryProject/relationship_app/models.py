# relationship_app/models.py

from django.db import models
from django.contrib.auth.models import User # Import Django's built-in User model
from django.db.models.signals import post_save # Import signal for automatic profile creation
from django.dispatch import receiver # Import receiver decorator for signals

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publication_year = models.IntegerField(null=True, blank=True) # <--- Add this line

    def __str__(self):
        return self.title


class Library(models.Model):
    name = models.CharField(max_length=100)
    # ManyToManyField: A library can have many books, and a book can be in many libraries.
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    # OneToOneField: A librarian is responsible for one specific library, and a library has one librarian.
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return self.name

# UserProfile Model for Role-Based Access Control
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username}'s Profile ({self.role})"
