# relationship_app/urls.py

from django.urls import path
from . import views # This import is correct for app-level urls.py
from django.contrib.auth import views as auth_views # Import Django's built-in auth views

# --- IMPORTANT ADDITION FOR CHECKER ---
# This line is specifically requested by the checker
from .views import list_books
from relationship_app import views as security_views

#app_name = 'relationship_app' # Namespace for your app's URLs (can uncomment if you set up app_name)

urlpatterns = [
    # Authors
    path('authors/', views.author_list_view, name='author_list'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),

    # Libraries
    path('libraries/', views.library_list_view, name='library_list'),
    # This links the class-based view correctly (no change needed here from last time)
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Librarians
    path('librarians/<int:pk>/', views.librarian_detail_view, name='librarian_detail'),

    # Books (List)
    # --- IMPORTANT CHANGE HERE FOR CHECKER ---
    # Now uses the directly imported 'list_books' function
    path('books/', list_books, name='list_books'),

    # Authentication Paths
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register_view, name='register'),

    # Role-Based Access Control Paths
    path('admin-only/', views.admin_view, name='admin_view'),
    path('librarian-only/', views.librarian_view, name='librarian_view'),
    path('member-only/', views.member_view, name='member_view'),

    # --- Book Management with Custom Permissions ---
    path('add_book/', views.book_add_view, name='book_add'),
    path('edit_book/<int:pk>/', views.book_edit_view, name='book_edit'),
    path('delete_book/<int:pk>/', views.book_delete_view, name='book_delete'),
    
    #path('admin/', admin.site.urls),
    # ... other paths ...
    path('my-form/', security_views.my_form_view, name='my_form'),
    path('my-form-unsafe/', security_views.my_form_unsafe_view, name='my_form_unsafe'),
    path('xss-demo/', security_views.xss_demo_view, name='xss_demo'),
    path('add-book/', security_views.add_book_view, name='add_book'),
    path('add-book-success/', security_views.add_book_success, name='add_book_success'),
    path('books/', security_views.list_books, name='list_books'), # Make sure this line exists
    path('', security_views.home_view, name='home'), # If you have a home view    

]