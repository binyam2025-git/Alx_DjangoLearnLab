# relationship_app/urls.py
from django.urls import path
from . import views

app_name = 'relationship_app' # Important for namespacing

urlpatterns = [
    path('authors/', views.author_list_view, name='author_list'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('libraries/', views.library_list_view, name='library_list'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('librarians/<int:pk>/', views.librarian_detail_view, name='librarian_detail'),
    path('books/', views.book_list_view, name='book_list'), # This is the new book list view
]