from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library # <--- THIS IS THE CORRECTED LINE

# Function-based View: Lists all books
def book_list(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)

# Class-based View: Displays details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    # Optional: Override get_context_data if you need additional data
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # The 'library' object is already available as self.object
    #     # You can add more context if needed, e.g., books related to this library
    #     # context['books_in_library'] = self.object.books.all()
    #     return context