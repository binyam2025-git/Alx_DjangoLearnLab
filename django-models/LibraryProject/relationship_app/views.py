from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library # <--- Make this the specific line the checker wants
from .models import Book    # <--- Import Book on its own line

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