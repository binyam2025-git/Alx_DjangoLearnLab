# C:\Users\user\Alx_DjangoLearnLab\advanced_features_and_security\LibraryProject\relationship_app\admin.py

from django.contrib import admin
# Import models defined in *this* app's models.py
from .models import Author, Library, Librarian, Member

# Register models from *this* app's models.py with the admin site
admin.site.register(Author)
admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(Member)

# IMPORTANT: The 'Book' model is usually defined in 'bookshelf/models.py'.
# It should typically be registered in 'bookshelf/admin.py'.
# If you had 'from .models import Book' or 'admin.site.register(Book)'
# in *this* file (relationship_app/admin.py), remove it to avoid confusion.