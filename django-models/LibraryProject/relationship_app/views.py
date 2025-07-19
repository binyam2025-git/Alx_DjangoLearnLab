# relationship_app/views.py

from django.shortcuts import render, get_object_or_404
# Import ListView and DetailView for generic class-based views
from django.views.generic.list import ListView      # This is for list views, if you use them
from django.views.generic.detail import DetailView # This is the exact import your checker wants
# Import your models
from .models import Author, Book, Library, Librarian


# --- Function-Based View: List all Authors ---
def author_list_view(request):
    authors = Author.objects.all().order_by('name')
    context = {
        'authors': authors
    }
    return render(request, 'relationship_app/author_list.html', context)

# --- Class-Based View: Author Detail ---
# Inherits from DetailView for single object display
class AuthorDetailView(DetailView):
    model = Author # Specify the model this view will operate on
    template_name = 'relationship_app/author_detail.html'
    context_object_name = 'author' # Name of the variable in the template (e.g., {{ author.name }})

    # If you need to pass related objects to the template, you can override get_context_data
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # Example: context['books'] = self.object.books.all() # Assuming 'books' is a related_name
    #     return context


# --- Function-Based View: List all Libraries ---
def library_list_view(request):
    libraries = Library.objects.all().order_by('name')
    context = {
        'libraries': libraries
    }
    return render(request, 'relationship_app/library_list.html', context)

# --- Class-Based View: Library Detail ---
# Inherits from DetailView for single object display
class LibraryDetailView(DetailView):
    model = Library # Specify the model this view will operate on
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library' # Name of the variable in the template (e.g., {{ library.name }})

    # If you need to pass related objects to the template, you can override get_context_data
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # Example: context['librarians'] = self.object.librarian_set.all()
    #     return context


# --- Function-Based View: Librarian Detail ---
def librarian_detail_view(request, pk):
    librarian = get_object_or_404(Librarian, pk=pk)
    context = {
        'librarian': librarian
    }
    return render(request, 'relationship_app/librarian_detail.html', context)


# --- Function-Based View: List all Books ---
def book_list_view(request):
    books = Book.objects.all().order_by('title')
    context = {
        'books': books
    }
    # Ensure this template name matches your actual template file for listing books
    return render(request, 'relationship_app/list_books.html', context)