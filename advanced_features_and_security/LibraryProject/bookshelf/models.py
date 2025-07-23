# C:\Users\user\Alx_DjangoLearnLab\advanced_features_and_security\LibraryProject\bookshelf\models.py

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

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

class CustomUser(AbstractUser):
    username = None # Remove default username
    email = models.EmailField(_('email address'), unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth'] # Example: prompt for date_of_birth when creating superuser

    objects = CustomUserManager()

    def __str__(self):
        return self.email

# (Leave this file focused on CustomUser for now. Other models like Book, Author, etc. should remain in relationship_app/models.py)

class Book(models.Model):
    # ... your fields ...
    class Meta:
        permissions = [
            ("can_view", "Can view book data"),
            ("can_create", "Can create new books"), # <--- CHECK THIS EXACTLY
            ("can_edit", "Can edit existing books"),
            ("can_delete", "Can delete books"),     # <--- CHECK THIS EXACTLY
        ]
        # ... other Meta options ...
    # ... __str__ method ...