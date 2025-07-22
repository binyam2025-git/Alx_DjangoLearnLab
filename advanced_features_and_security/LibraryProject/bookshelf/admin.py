# C:\Users\user\Alx_DjangoLearnLab\advanced_features_and_security\LibraryProject\bookshelf\admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin # Keep this import
from .models import CustomUser # Import CustomUser from this app's models

class CustomUserAdmin(UserAdmin):
    # The 'username' field is not used, so we override the default UserAdmin fieldsets
    # to remove it and ensure 'email' is the primary identifier.

    # Fieldsets for changing an existing user (detail view)
    fieldsets = (
        (None, {'fields': ('email', 'password')}), # Use 'email' instead of 'username'
        ('Personal info', {'fields': ('date_of_birth', 'profile_photo', 'first_name', 'last_name')}), # Add first_name, last_name if you want to display them
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Fieldsets for adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'password2'), # Use 'email' instead of 'username'
        }),
        ('Personal info', {'fields': ('date_of_birth', 'profile_photo', 'first_name', 'last_name')}), # Add first_name, last_name if you want
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    # Fields to display in the list view of users
    list_display = ('email', 'date_of_birth', 'is_staff') # Use 'email' instead of 'username'
    search_fields = ('email',) # Search by email
    ordering = ('email',) # Order by email

admin.site.register(CustomUser, CustomUserAdmin)
