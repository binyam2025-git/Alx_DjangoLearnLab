# relationship_app/urls.py

from django.urls import path
from . import views # This import is correct for app-level urls.py

app_name = 'relationship_app' # Namespace for your app's URLs

urlpatterns = [
    # Authors
    path('authors/', views.author_list_view, name='author_list'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),

    # Libraries
    path('libraries/', views.library_list_view, name='library_list'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Librarians
    path('librarians/<int:pk>/', views.librarian_detail_view, name='librarian_detail'),

    # Books (List)
    path('books/', views.book_list_view, name='book_list'),

    # Add other specific paths here if you have them,
    # e.g., for book details, etc., as per your project requirements.
]