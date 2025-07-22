# C:\Users\user\Alx_DjangoLearnLab\advanced_features_and_security\LibraryProject\bookshelf\admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser # Import CustomUser from this app's models

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    list_display = ('email', 'date_of_birth', 'is_staff')
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
