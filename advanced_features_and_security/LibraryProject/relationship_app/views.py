
# C:\Users\user\Alx_DjangoLearnLab\advanced_features_and_security\LibraryProject\relationship_app\views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
# --- ADD THIS IMPORT ---
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView # Add DetailView, and potentially others if you use them


# --- THESE ARE THE TWO CORRECT IMPORT LINES YOU NEED ---
# Import models that are defined WITHIN 'relationship_app/models.py'
from .models import Author, Library, Librarian, Member # Adjust to include ALL models truly defined in your relationship_app/models.py

# Import the Book model from the 'bookshelf' app's models.py (if relationship_app views need it)
from bookshelf.models import Book

# ... (then follow with your other imports like forms, and your view functions) ...


# --- All book-related views are REMOVED from this file as per instructions ---
# These views (list_books, book_add_view, add_book_success, book_edit_view, book_delete_view)
# should now primarily reside in the 'bookshelf' app's views.py.
# -----------------------------------------------------------------------------


def home_view(request):
    """
    Renders the home page for the relationship_app.
    """
    return render(request, 'relationship_app/home.html')

def register_view(request):
    """
    Handles user registration.
    This is a placeholder; you would implement your actual registration logic here.
    """
    # Example placeholder for a registration view
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home') # Redirect to home or a success page
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# Your user group checking functions
def is_admin(user):
    """Checks if the user belongs to the 'Admins' group."""
    return user.groups.filter(name='Admins').exists()

def is_librarian(user):
    """
    Checks if the user belongs to the 'Librarians' group.
    Assumes you have a 'Librarians' group, otherwise adjust the group name.
    """
    return user.groups.filter(name='Librarians').exists()

def is_member(user):
    """
    Checks if the user belongs to the 'Members' group.
    Assumes you have a 'Members' group, otherwise adjust the group name.
    """
    return user.groups.filter(name='Members').exists()

@login_required
def admin_view(request):
    """
    View accessible only by users in the 'Admins' group.
    """
    if is_admin(request.user):
        return HttpResponse("Welcome, Admin!")
    return HttpResponseForbidden("You are not authorized to view this page.")

@login_required
def librarian_view(request):
    """
    View accessible only by users in the 'Librarians' group.
    """
    if is_librarian(request.user):
        return HttpResponse("Welcome, Librarian!")
    return HttpResponseForbidden("You are not authorized to view this page.")

@login_required
def member_view(request):
    """
    View accessible only by users in the 'Members' group.
    """
    if is_member(request.user):
        return HttpResponse("Welcome, Member!")
    return HttpResponseForbidden("You are not authorized to view this page.")

def author_list_view(request):
    """
    Lists all authors.
    """
    authors = Author.objects.all()
    return render(request, 'relationship_app/author_list.html', {'authors': authors})

class AuthorDetailView(DetailView):
    """
    Displays details of a single author.
    """
    model = Author
    template_name = 'relationship_app/author_detail.html'

def library_list_view(request):
    """
    Lists all libraries.
    """
    libraries = Library.objects.all()
    return render(request, 'relationship_app/library_list.html', {'libraries': libraries})

class LibraryDetailView(DetailView):
    """
    Displays details of a single library.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'

def librarian_detail_view(request, pk):
    """
    Displays details of a single librarian.
    """
    librarian = get_object_or_404(Librarian, pk=pk)
    return render(request, 'relationship_app/librarian_detail.html', {'librarian': librarian})

# You might have other security demo views as well:
def my_form_view(request):
    """
    Placeholder for a general form view.
    """
    return HttpResponse("This is a placeholder for a secure form view.")

def my_form_unsafe_view(request):
    """
    Placeholder for a potentially unsafe form view (for demonstration purposes, not for actual use).
    """
    return HttpResponse("This is a placeholder for a potentially unsafe form view for security demos.")

def xss_demo_view(request):
    """
    Placeholder for an XSS demonstration view.
    """
    # Example: If you wanted to show XSS vulnerability before full protection
    # user_input = request.GET.get('input', 'Default')
    # return HttpResponse(f"<h1>{user_input}</h1>") # Unsafe!
    # With Django templates, it's typically safe by default:
    user_input = request.GET.get('input', 'Default')
    return render(request, 'relationship_app/xss_demo.html', {'user_input': user_input}) # Template should escape it