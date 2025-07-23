# C:\Users\user\Alx_DjangoLearnLab\advanced_features_and_security\LibraryProject\relationship_app\models.py

from django.db import models
from django.conf import settings # Keep this import for Librarian model
# from django.contrib.auth.models import AbstractUser, BaseUserManager # REMOVE THIS LINE if it's there
# from django.utils.translation import gettext_lazy as _ # REMOVE if only used for CustomUser

# --- REMOVE CustomUserManager and CustomUser classes entirely from this file ---
# class CustomUserManager(BaseUserManager):
#     ... (REMOVE THIS BLOCK) ...

# class CustomUser(AbstractUser):
#     ... (REMOVE THIS BLOCK) ...
# --------------------------------------------------------------------------

# --- Your other models (Book, Author, Library, Librarian) ---
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    library = models.ForeignKey('Library', on_delete=models.CASCADE)
    class Meta:
        permissions = [
             
            ("can_view_book", "Can view book data"), # For general viewing
            ("can_create_book", "Can create new books"),
            ("can_edit_book", "Can edit existing books"),
            ("can_delete_book", "Can delete a book"),
        ]
        verbose_name = "Book"
        verbose_name_plural = "Books"
    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Librarian(models.Model):
    # This MUST point to settings.AUTH_USER_MODEL
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.user.email