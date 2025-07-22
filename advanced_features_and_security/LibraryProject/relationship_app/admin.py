# C:\Users\user\Alx_DjangoLearnLab\advanced_features_and_security\LibraryProject\relationship_app\admin.py

from django.contrib import admin
# Make sure these are the ONLY models imported from .models
from .models import Author, Book, Library, Librarian

# Ensure no CustomUserAdmin class or UserAdmin import is here:
# class CustomUserAdmin(UserAdmin):
#     ... (REMOVE THIS BLOCK) ...

# Ensure no registration of CustomUser is here:
# admin.site.register(CustomUser, CustomUserAdmin)

# Register your other models as before:
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)