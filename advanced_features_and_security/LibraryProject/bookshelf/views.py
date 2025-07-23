# C:\Users\user\Alx_DjangoLearnLab\advanced_features_and_security\LibraryProject\bookshelf\views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse # Keep HttpResponse if used in add_book_success
from django.contrib.auth.decorators import login_required, permission_required
from bookshelf.models import Book, Author, Library # All related models are here now
from relationship_app.forms import BookForm # BookForm is still in relationship_app


@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request): # RENAMED from list_books
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books}) # Template path remains the same for now

@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def book_add_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list') # Redirect to the new name
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form, 'action': 'Add'})

# This view is purely for redirect success, doesn't need permissions
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
            return redirect('book_list') # Redirect to the new name
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_form.html', {'form': form, 'action': 'Edit'})

@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list') # Redirect to the new name
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})