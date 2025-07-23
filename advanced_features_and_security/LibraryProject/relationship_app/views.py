# C:\Users\user\Alx_DjangoLearnLab\advanced_features_and_security\LibraryProject\relationship_app\views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden # Add HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm # Use this or your custom form if you make one
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required # Ensure permission_required is here
from django.contrib.auth import login, authenticate, logout
from django.views.generic import DetailView, ListView
from django.conf import settings # Add this import for settings.AUTH_USER_MODEL (if needed)

# Import your models, explicitly CustomUser now
from .models import Author, Book, Librarian, Library # Make sure Book is imported
from .forms import BookForm # You'll need to create this later if you don't have it

# Optional: If you use a custom form for registration, define it here or import it.
# from .forms import CustomUserCreationForm # Example if you create a forms.py

# --- Helper functions for role checks (UPDATE THESE) ---
def is_admin(user):
    # For now, just check if user is superuser or staff
    return user.is_authenticated and user.is_superuser # or user.is_staff

def is_librarian(user):
    return user.is_authenticated and user.is_staff and not user.is_superuser # Example: staff but not superuser

def is_member(user):
    return user.is_authenticated and not user.is_staff and not user.is_superuser # Example: regular user

# --- Your existing views (UPDATE WHERE USER.USERPROFILE WAS USED) ---

def home_view(request):
    return render(request, 'relationship_app/home.html')

# Register view: Set role directly on CustomUser
def register_view(request):
    if request.method == 'POST':
        # Use UserCreationForm provided by Django Auth
        # Or if you created a custom form for CustomUser, use that: CustomUserCreationForm(request.POST)
        form = UserCreationForm(request.POST) # This form creates the base user fields
        if form.is_valid():
            user = form.save(commit=False)
            # Set default role here
            #user.role = 'Member' # Default role for new registrations
            user.save()

            # If you need to set date_of_birth or profile_photo during registration,
            # you'd need a custom registration form that includes those fields,
            # then save them to 'user' object directly.
            # Example (assuming your custom form has these fields):
            # user.date_of_birth = form.cleaned_data.get('date_of_birth')
            # user.profile_photo = form.cleaned_data.get('profile_photo')
            # user.save()

            login(request, user) # Automatically log in the user after registration
            return redirect('home') # Redirect to home or a success page
    else:
        form = UserCreationForm() # Or your custom registration form
    return render(request, 'registration/register.html', {'form': form})

# Example views requiring specific roles (UPDATED)
@login_required
@user_passes_test(is_admin, login_url='/login/') # Or a specific permission denied page
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian, login_url='/login/')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member, login_url='/login/')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# --- CSRF and XSS Demo Views (keep as is) ---
def my_form_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        return HttpResponse(f"Hello, {name}!")
    return render(request, 'relationship_app/my_form.html')

@csrf_exempt # For demonstration of unsafe view only, DO NOT use in production
def my_form_unsafe_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        return HttpResponse(f"Hello, {name} (unsafe)!")
    return render(request, 'relationship_app/my_form_unsafe.html')

def xss_demo_view(request):
    user_input = request.GET.get('q', 'No input provided.')
    context = {'user_input': user_input}
    return render(request, 'relationship_app/xss_demo.html', context)

# For adding a book (previously add_book_view, now renamed for clarity)
@login_required
@permission_required('relationship_app.can_create_book', raise_exception=True)
def book_add_view(request):
    # You'll need a form for this. Let's assume you'll create one.
    # For now, a placeholder to satisfy the view check:
    if request.method == 'POST':
        form = BookForm(request.POST) # You'll need to define this form
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form, 'action': 'Add'})

def add_book_success(request): # This view needs no permission as it's just a redirect target
    return HttpResponse("Book added successfully!")

@login_required
@permission_required('relationship_app.can_view_book', raise_exception=True)
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})

# For editing a book
@login_required
@permission_required('relationship_app.can_edit_book', raise_exception=True)
def book_edit_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_form.html', {'form': form, 'action': 'Edit'})

# For deleting a book
@login_required
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def book_delete_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})

# --- Author, Library, Librarian Views (verify they don't use UserProfile) ---
def author_list_view(request):
    authors = Author.objects.all()
    return render(request, 'relationship_app/author_list.html', {'authors': authors})

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'relationship_app/author_detail.html'
    context_object_name = 'author'

def library_list_view(request):
    libraries = Library.objects.all()
    return render(request, 'relationship_app/library_list.html', {'libraries': libraries})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def librarian_detail_view(request, pk):
    # Ensure this now correctly uses CustomUser if Librarian's FK is to CustomUser
    librarian = get_object_or_404(Librarian, pk=pk)
    return render(request, 'relationship_app/librarian_detail.html', {'librarian': librarian})