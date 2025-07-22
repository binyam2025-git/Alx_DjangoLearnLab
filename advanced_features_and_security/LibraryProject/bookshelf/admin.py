from django.contrib import admin

# Register your models here.
from .models import Book # Import your Book model

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year') # Display these fields in the list view
    list_filter = ('publication_year', 'author') # Add filters for these fields
    search_fields = ('title', 'author') # Enable search by title and author

admin.site.register(Book, BookAdmin)

