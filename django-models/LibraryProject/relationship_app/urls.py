# relationship_app/urls.py

from django.urls import path
from . import views # This import is correct for app-level urls.py
from django.contrib.auth import views as auth_views # Import Django's built-in auth views

#app_name = 'relationship_app' # Namespace for your app's URLs

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
    # ... your existing paths ...

    # Authentication Paths
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'), # Redirects to home or login page
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register_view, name='register'),
]