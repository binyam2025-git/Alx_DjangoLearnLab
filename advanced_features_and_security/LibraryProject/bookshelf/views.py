# C:\Users\user\Alx_DjangoLearnLab\advanced_features_and_security\LibraryProject\bookshelf\views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required

# Import the BookForm from the SAME app (bookshelf)
from .forms import BookForm # Corrected: BookForm and ExampleForm are in this app's forms.py
from .forms import ExampleForm 

# Import models from their definitive location: relationship_app
from relationship_app.models import Book, Author, Library
from rest_framework import generics, viewsets
from .models import Book, Author, Comment
from .serializers import BookSerializer, AuthorSerializer, CommentSerializer
from .permissions import IsPremiumUser


from rest_framework.decorators import action # <-- Import action for custom methods
from rest_framework.response import Response
from rest_framework import status # For HTTP status codes
from rest_framework import permissions


# View for Author (optional, but good for completeness)
class AuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# ListCreateAPIView provides GET (list all books) and POST (create a new book)
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all() # The queryset for fetching objects
    queryset = Book.objects.select_related('author')
    serializer_class = BookSerializer # The serializer to use for data conversion

    def get_queryset(self):
        # Start with the base queryset (all books)
        queryset = super().get_queryset()

        # --- Filtering Logic ---
        # Get the 'author_name' query parameter from the request, if it exists
        author_name = self.request.query_params.get('author_name', None)
        if author_name is not None:
            # Filter books where the author's name contains the provided string (case-insensitive)
            queryset = queryset.filter(author__name__icontains=author_name)

        # You could add other filters here, e.g., by title:
        # title_contains = self.request.query_params.get('title_contains', None)
        # if title_contains is not None:
        #     queryset = queryset.filter(title__icontains=title_contains)

        # --- QuerySet Optimization (Next Step) ---
        # For now, return the potentially filtered queryset
        return queryset

        # --- Filtering Logic ---
        author_name = self.request.query_params.get('author_name', None)
        if author_name is not None:
            queryset = queryset.filter(author__name__icontains=author_name)

        # Return the optimized and potentially filtered queryset
        return queryset

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # Apply permissions here
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions] # <-- ADDED PERMISSION
    
    def get_permissions(self):
        if self.action == 'create':
            # For 'create' action, require IsAuthenticated AND IsPremiumUser
            return [permissions.IsAuthenticated(), IsPremiumUser()]
        elif self.action == 'flag': # Assuming 'flag' action needs staff
            return [permissions.IsAuthenticated(), permissions.IsAdminUser()]
        # For all other actions (list, retrieve, update, delete), use default permissions
        return super().get_permissions()

    # Custom action to flag a comment
    # Detail=True means this action applies to a specific instance (e.g., /comments/1/flag/)
    @action(detail=True, methods=['post'])
    def flag(self, request, pk=None):
        # For custom actions, you might want specific permissions
        # E.g., only staff can flag:
        if not request.user.is_staff:
            return Response({'detail': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
        comment = self.get_object() # Get the specific comment instance
        comment.flagged = True
        comment.save()
        serializer = self.get_serializer(comment) # Serialize the updated comment
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Optional: You might want to filter comments by book
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     book_pk = self.request.query_params.get('book', None)
    #     if book_pk is not None:
    #         queryset = queryset.filter(book__pk=book_pk)
    #     return queryset

# RetrieveUpdateDestroyAPIView provides GET (single book), PUT/PATCH (update), DELETE
class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

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