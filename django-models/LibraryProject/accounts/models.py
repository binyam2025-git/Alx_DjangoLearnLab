# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any custom fields you have here, e.g.,
    # date_of_birth = models.DateField(null=True, blank=True)
    # profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    # Add or modify these fields if they are explicitly defined in CustomUser
    # If CustomUser is subclassing AbstractUser directly, you usually *don't*
    # need to explicitly define these fields. The fix for E304 is often
    # simply adding the related_name arguments within the AbstractUser class
    # or ensuring your custom user model definition is correct.

    # However, if you have explicitly overridden these fields for some reason,
    # or if Django's internal checks are getting confused,
    # adding related_name is the solution.

    # This is the most common way to fix E304 for custom user models:
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="customuser_set", # <--- ADD THIS RELATED_NAME
        related_query_name="customuser",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_permissions_set", # <--- ADD THIS RELATED_NAME
        related_query_name="customuser_permission",
    )

    # Add your custom methods or fields below this line if any
    # e.g., def __str__(self): return self.username
