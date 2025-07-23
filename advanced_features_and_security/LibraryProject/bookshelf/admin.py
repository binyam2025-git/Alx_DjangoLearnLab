# C:\Users\user\Alx_DjangoLearnLab\advanced_features_and_security\LibraryProject\bookshelf\admin.py

from django.contrib import admin

# Import models that belong to the 'bookshelf' app and need to be registered in the admin.
# Based on your previous models.py corrections, 'Book' is a primary model in 'bookshelf'.
# If 'Author' is also truly defined in 'bookshelf/models.py' and not just 'relationship_app/models.py',
# then uncomment it. However, typically models are defined in one place.
from .models import Book
# from .models import Author # Uncomment if Author model is also specifically in bookshelf/models.py

# --- REMOVED CustomUserAdmin class and CustomUser registration ---
# These belong in accounts/admin.py, where CustomUser is defined and managed.
# All lines related to CustomUser import, CustomUserAdmin class,
# and admin.site.register(CustomUser, CustomUserAdmin) have been removed from this file.
# ------------------------------------------------------------------

# Register your models from the 'bookshelf' app here.
# This makes them visible and manageable in the Django admin interface.
admin.site.register(Book)

# If you uncommented Author above, uncomment this line too.
# admin.site.register(Author)

# Example for other models if you were to add them to bookshelf app:
# from .models import Genre, Tag
# admin.site.register(Genre)
# admin.site.register(Tag)