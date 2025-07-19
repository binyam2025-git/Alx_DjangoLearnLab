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

    # Authentication Paths
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register_view, name='register'),

    # Role-Based Access Control Paths
    path('admin-only/', views.admin_view, name='admin_view'),
    path('librarian-only/', views.librarian_view, name='librarian_view'),
    path('member-only/', views.member_view, name='member_view'),

    # --- Book Management with Custom Permissions ---
    # These paths link to the new views that enforce permissions
    path('books/add/', views.book_add_view, name='book_add'),
    path('books/<int:pk>/edit/', views.book_edit_view, name='book_edit'),
    path('books/<int:pk>/delete/', views.book_delete_view, name='book_delete'),
]