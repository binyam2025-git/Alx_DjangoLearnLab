# LibraryProject/bookshelf/views.py
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt # Temporarily for demonstration only!
from .forms import BookForm # This import will be needed in Phase 2

# ... (Keep any existing views you have here, e.g., for restricted-add-book) ...

# --- VIEWS FOR CSRF AND XSS DEMONSTRATION ---

def my_form_view(request):
    """
    A simple form demonstrating Django's built-in CSRF protection.
    """
    message = ""
    if request.method == 'POST':
        message = "Form submitted successfully with CSRF protection!"
    else:
        message = "Please submit the form (CSRF protected)."
    return render(request, 'bookshelf/my_form.html', {'message': message})

@csrf_exempt # WARNING: ONLY for demonstrating lack of CSRF protection. Do NOT use in production!
def my_form_view_unsafe(request):
    """
    A simple form demonstrating a lack of CSRF protection (due to @csrf_exempt).
    """
    message = ""
    if request.method == 'POST':
        message = "Unsafe form submitted (CSRF bypassed)!"
    else:
        message = "Please submit the unsafe form (NO CSRF protection)."
    return render(request, 'bookshelf/my_form_unsafe.html', {'message': message})

def xss_demo_view(request):
    """
    A view to demonstrate Django's XSS protection (auto-escaping).
    """
    # This string contains malicious script that Django should escape
    user_input_with_script = "<script>alert('You have been XSSed!');</script><h1>Malicious Content!</h1>"
    return render(request, 'bookshelf/xss_demo.html', {'user_content': user_input_with_script})

# --- VIEW FOR INPUT VALIDATION (Phase 2) ---

def book_create_view(request):
    """
    A view for creating a Book demonstrating input validation.
    """
    message = ""
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Book added successfully with validation!"
            # Consider redirecting here in a real app
        else:
            message = "Validation errors occurred. Please correct the form."
    else:
        form = BookForm()
        message = "Fill out the form to add a book (with validation)."
    return render(request, 'bookshelf/book_form.html', {'form': form, 'message': message})