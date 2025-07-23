# C:\Users\user\Alx_DjangoLearnLab\advanced_features_and_security\LibraryProject\accounts\models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any additional fields you want for your user here.
    # For now, 'pass' is fine if you don't need extra fields yet.
    pass

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'

    def __str__(self):
        return self.username