# C:\Users\user\Alx_DjangoLearnLab\advanced_features_and_security\LibraryProject\bookshelf\views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required

# Import the BookForm from the SAME app (bookshelf)
from .forms import BookForm, ExampleForm # Corrected: BookForm and ExampleForm are in this app's forms.py

# Import models from their definitive location: relationship_app
from relationship_app.models import Book, Author, Library

@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    # Ensure template path is correct relative to the 'templates' directory in your project
    # or if 'bookshelf' has its own templates folder, ensure it's configured in settings.py
    return render(request, 'bookshelf/book_list.html', {'books': books}) # Confirmed template path

@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def book_add_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form, 'action': 'Add'}) # Confirmed template path

def add_book_success(request):
    return HttpResponse("Book added successfully!")

@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/book_form.html', {'form': form, 'action': 'Edit'}) # Confirmed template path

@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book}) # Confirmed template path

def form_example_view(request):
    """
    Handles the ExampleForm to demonstrate secure input rendering.
    """
    processed_input = None
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Django's template engine automatically escapes HTML by default.
            # This prevents basic XSS attacks by rendering script tags as plain text.
            # Assuming 'user_input' is a field in ExampleForm (e.g., your_name or message)
            # We'll use 'your_name' as an example based on your forms.py
            processed_input = form.cleaned_data['your_name']
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {
        'form': form,
        'processed_input': processed_input
    })