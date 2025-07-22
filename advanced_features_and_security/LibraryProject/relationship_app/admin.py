# C:\Users\user\Alx_DjangoLearnLab\advanced_features_and_security\LibraryProject\relationship_app\admin.py

from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
from .models import Author, Book, Library, Librarian # Import your models

class CustomUserAdmin(UserAdmin):
    # Add date_of_birth and profile_photo to the fieldsets
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    # Add these fields to the form when creating a new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    # If you removed the 'username' field and use 'email' as USERNAME_FIELD:
    list_display = ('email', 'date_of_birth', 'is_staff') # Use 'email' instead of 'username'
    search_fields = ('email',) # Search by email instead of username
    ordering = ('email',) # Order by email

# Unregister the default User model if it was implicitly registered
# (though often not strictly necessary if CustomUser replaces it cleanly)
# from django.contrib.auth.models import User
# try:
#     admin.site.unregister(User)
# except admin.sites.NotRegistered:
#     pass

admin.site.register(CustomUser, CustomUserAdmin)

# Register your other models as before
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
# If you still have a UserProfile, register it here as well
# admin.site.register(UserProfile)