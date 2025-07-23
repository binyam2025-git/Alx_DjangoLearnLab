# C:\Users\user\Alx_DjangoLearnLab\advanced_features_and_security\LibraryProject\relationship_app\models.py

from django.db import models
from django.conf import settings # Keep this import for Librarian and Member models

# ----------------------------------------------------------------------
# Define models that are referenced by others FIRST (e.g., Author, Library)
# This prevents NameError due to forward references.
# ----------------------------------------------------------------------

class Author(models.Model):
    name = models.CharField(max_length=100)
    # Add any other fields specific to an Author if needed, e.g., biography, birth_date
    # biography = models.TextField(blank=True, null=True)
    # birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Library(models.Model):
    name = models.CharField(max_length=200) # Increased max_length slightly for more flexibility
    location = models.CharField(max_length=255, blank=True, null=True)
    # Add any other fields specific to a Library if needed, e.g., contact_info, capacity
    # contact_email = models.EmailField(blank=True, null=True)
    # capacity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

# ----------------------------------------------------------------------
# Define models that reference previously defined models, or are top-level
# ----------------------------------------------------------------------

class Book(models.Model):
    title = models.CharField(max_length=200)
    # Author and Library are defined above, so no quotes are needed (though quotes are also valid)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='relationship_books')
    library = models.ForeignKey(Library, on_delete=models.SET_NULL, null=True, blank=True, related_name='books_in_library')

    # All these fields are correctly activated and present as per requirements
    publication_date = models.DateField(null=True, blank=True)
    genre = models.CharField(max_length=100, blank=True, null=True)
    isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

# Librarian and Member reference settings.AUTH_USER_MODEL, so they can come here
class Librarian(models.Model):
    # This is correctly defined without primary_key=True on the user field
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=50, unique=True, blank=True, null=True)
    # Example link to Library (uncomment if you need it)
    # library = models.ForeignKey(Library, on_delete=models.SET_NULL, null=True, blank=True, related_name='librarians')

    def __str__(self):
        # A more descriptive __str__ method, useful for debugging and admin display
        return f"Librarian: {self.user.username}"

class Member(models.Model):
    # This is also correctly defined without primary_key=True on the user field
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Add other member-specific fields here
    membership_id = models.CharField(max_length=50, unique=True, blank=True, null=True)
    # Example many-to-many relationship with Book (uncomment if you need it)
    # borrowed_books = models.ManyToManyField(Book, related_name='borrowers', blank=True)

    def __str__(self):
        # A more descriptive __str__ method
        return f"Member: {self.user.username}"