# C:\Users\user\Alx_DjangoLearnLab\advanced_features_and_security\LibraryProject\relationship_app\models.py

from django.contrib.auth.models import AbstractUser, BaseUserManager # Import BaseUserManager here
from django.db import models
from django.utils import timezone # Import timezone for default date values if needed
from django.utils.translation import gettext_lazy as _ # Good practice for verbose names
from django.conf import settings # Add this import!


# --- Custom User Manager (will be defined in Step 3, but declare now) ---
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)


# --- Custom User Model ---
class CustomUser(AbstractUser):
    # Remove username if you want to use email as unique identifier
    # username = None # Uncomment this if you want to remove the default username field

    email = models.EmailField(_('email address'), unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    # Set email as the unique identifier for authentication
    # If you remove username, you MUST set a new USERNAME_FIELD
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS are fields prompted when creating a superuser (excluding password and USERNAME_FIELD)
    REQUIRED_FIELDS = ['date_of_birth'] # Example: prompt for date_of_birth when creating superuser

    # Link the custom manager to your custom user model
    objects = CustomUserManager()

    # Add related_name to avoid clashes if you had a UserProfile previously
    # If you previously had a UserProfile with a OneToOneField to User,
    # and it used related_name='userprofile', you might need to adjust or remove that.
    # For simplicity, if this is a fresh start for custom user model, we're putting fields directly here.

    def __str__(self):
        return self.email

# --- Your existing models (Book, Author, Library, Librarian, UserProfile - if still in use) ---
# Make sure to adjust any ForeignKeys or OneToOneFields that previously pointed to
# django.contrib.auth.models.User to now point to settings.AUTH_USER_MODEL.
# We will specifically address this in Step 5.

# Example: If you have a Book model that has an 'owner' field
class Book(models.Model):
    title = models.CharField(max_length=200)
    # Assuming you have Author and Library models
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    library = models.ForeignKey('Library', on_delete=models.CASCADE)
    # Example of a FK to the custom user model:
    # borrowed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        permissions = [
            ("can_add_book", "Can add a new book"),
            ("can_change_book", "Can change existing book data"),
            ("can_delete_book", "Can delete a book"),
        ]

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
    # Ensure this points to the CustomUser
    #user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.user.email # Use email as identifier

# If you still need a UserProfile for additional *non-authentication* related fields
# that are not part of the core CustomUser, keep it. But for fields like 'role',
# it might be simpler to integrate them directly into CustomUser for this exercise.
# If you kept UserProfile, ensure its 'user' field points to CustomUser.
# class UserProfile(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='user_profile')
#     # ... other fields
#     def __str__(self):
#         return self.user.email