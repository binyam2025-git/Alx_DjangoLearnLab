# C:\Users\user\Alx_DjangoLearnLab\advanced_features_and_security\LibraryProject\bookshelf\models.py

from django.db import models
from django.conf import settings
import datetime # <-- Make sure this import is here for the date default
from django.contrib.auth.models import User
from django.conf import settings


# --- Author Model (MUST be defined BEFORE Book, as Book depends on it) ---
class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # Add any other fields you want for Author here, e.g.,
    # biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# --- Book Model ---
class Book(models.Model):
    # Add a default for 'title' here. An empty string is often suitable for CharFields.
    title = models.CharField(max_length=200, default='Untitled Book') # <-- ADD THIS DEFAULT
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='bookshelf_books')
    # Ensure the default is still here for 'published_date' (or 'publication_date')
    published_date = models.DateField(default=datetime.date(2000, 1, 1)) # <-- CONFIRM THIS DEFAULT
    isbn = models.CharField(max_length=13, unique=True, blank=True, null=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author.name}"
    
    def days_since_published(self):
        # Calculate the difference between today and the published date
        # We use timezone.localdate() for current date to be timezone-aware
        # if your settings use TIME_ZONE, otherwise datetime.date.today() is fine
        # Let's use datetime.date.today() for simplicity if you're not deeply into timezones yet
        today = datetime.date.today()
        if self.published_date:
            # Returns a timedelta object, we need its .days attribute
            return (today - self.published_date).days
        return None # Or 0, or handle as appropriate if published_date can be null

class Comment(models.Model):
    book = models.ForeignKey(
        'Book',                 # Link to the Book model
        on_delete=models.CASCADE,
        related_name='comments' # Allows book.comments.all()
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, # Link to the User model
        on_delete=models.CASCADE,
        related_name='comments',
        null=True, # Allow comments without a specific user for now (e.g., anonymous)
        blank=True
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Added for the custom action:
    flagged = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment by {self.user.username if self.user else 'Anonymous'} on {self.book.title[:30]}..."

    class Meta:
        ordering = ['-created_at'] # Order comments by most recent first
class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, # <-- CHANGE THIS LINE
        on_delete=models.CASCADE,
        related_name='profile'
    )
    is_premium = models.BooleanField(default=False)
    # Add other profile fields here as needed (e.g., bio, avatar)

    def __str__(self):
        return f"{self.user.username}'s Profile"