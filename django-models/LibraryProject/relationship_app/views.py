from django.shortcuts import render
from django.views.generic import DetailView # Corrected from ListView as task asks for specific library detail
from .models import Book, Library # Import your models

# Function-based View: Lists all books
def book_list(request):
    books = Book.objects.all() # Get all Book objects from the database
    context = {
        'books': books
    }
    # Render the list_books.html template
    return render(request, 'relationship_app/list_books.html', context)

# Class-based View: Displays details for a specific library
class LibraryDetailView(DetailView): # Using DetailView for a single object's details
    model = Library # The model this view operates on
    template_name = 'relationship_app/library_detail.html' # Template to render
    context_object_name = 'library' # Name of the variable in the template context

    # Optional: Override get_context_data if you need additional data
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # The 'library' object is already available as self.object
    #     # You can add more context if needed, e.g., books related to this library
    #     # context['books_in_library'] = self.object.books.all()
    #     return context