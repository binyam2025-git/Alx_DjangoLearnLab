# C:\Users\user\Alx_DjangoLearnLab\advanced_features_and_security\LibraryProject\relationship_app\views.py

from django.shortcuts import render, redirect, get_object_or_404
# Removed HttpResponse, HttpResponseForbidden if not used by remaining views
from django.contrib.auth.decorators import login_required # Keep if home/register need it
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
# Removed from .forms import BookForm, as it's not used by remaining views here
from bookshelf.models import Author, Library # Keep these if used by remaining views
from .models import Librarian # Keep this

from django.views.generic import DetailView # Keep if used by remaining views

# --- REMOVE all book-related views from this file: ---
# @permission_required(...)
# def list_books(request): ...
# @permission_required(...)
# def book_add_view(request): ...
# def add_book_success(request): ...
# @permission_required(...)
# def book_edit_view(request, pk): ...
# @permission_required(...)
# def book_delete_view(request, pk): ...
# -----------------------------------------------------

# Keep your other views here, e.g.:
def home_view(request):
    return render(request, 'relationship_app/home.html')

def register_view(request):
    # ... (your registration view code) ...
    pass

# Your user group checking functions
def is_admin(user):
    return user.groups.filter(name='Admins').exists()

def is_librarian(user):
    return user.groups.filter(name='Librarians').exists() # Assuming you have a 'Librarians' group, otherwise adjust

def is_member(user):
    return user.groups.filter(name='Members').exists() # Assuming you have a 'Members' group, otherwise adjust

@login_required
def admin_view(request):
    if is_admin(request.user):
        return HttpResponse("Welcome, Admin!")
    return HttpResponseForbidden("You are not authorized to view this page.")

@login_required
def librarian_view(request):
    if is_librarian(request.user):
        return HttpResponse("Welcome, Librarian!")
    return HttpResponseForbidden("You are not authorized to view this page.")

@login_required
def member_view(request):
    if is_member(request.user):
        return HttpResponse("Welcome, Member!")
    return HttpResponseForbidden("You are not authorized to view this page.")

def author_list_view(request):
    authors = Author.objects.all()
    return render(request, 'relationship_app/author_list.html', {'authors': authors})

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'relationship_app/author_detail.html'

def library_list_view(request):
    libraries = Library.objects.all()
    return render(request, 'relationship_app/library_list.html', {'libraries': libraries})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

def librarian_detail_view(request, pk):
    librarian = get_object_or_404(Librarian, pk=pk)
    return render(request, 'relationship_app/librarian_detail.html', {'librarian': librarian})

# You might have other security demo views as well:
def my_form_view(request):
    # ...
    pass
def my_form_unsafe_view(request):
    # ...
    pass
def xss_demo_view(request):
    # ...
    pass