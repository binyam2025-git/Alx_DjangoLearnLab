# C:\Users\user\Alx_DjangoLearnLab\advanced_features_and_security\LibraryProject\LibraryProject\urls.py
from django.contrib import admin
from django.urls import path, include # <--- ADD ', include' HERE
from relationship_app import views as security_views # Import views directly

urlpatterns = [
    path('admin/', admin.site.urls),

    # Removed: path('relationships_app/', include('relationship_app.urls')),

    # Direct paths for the security demonstrations and core app views
    # Ensure these functions exist in relationship_app/views.py
    path('my-form/', security_views.my_form_view, name='my_form'),
    path('my-form-unsafe/', security_views.my_form_unsafe_view, name='my_form_unsafe'),
    path('xss-demo/', security_views.xss_demo_view, name='xss_demo'),
    path('add-book/', security_views.book_add_view, name='add_book'), # Make sure this matches `book_add_view` in views.py
    path('add-book-success/', security_views.add_book_success, name='add_book_success'),
    path('books/', security_views.list_books, name='list_books'),

    # Core app views (ensure these are also imported or handled)
    path('', security_views.home_view, name='home'),
    path('authors/', security_views.author_list_view, name='author_list'),
    path('authors/<int:pk>/', security_views.AuthorDetailView.as_view(), name='author_detail'),
    path('libraries/', security_views.library_list_view, name='library_list'),
    path('libraries/<int:pk>/', security_views.LibraryDetailView.as_view(), name='library_detail'),
    path('librarians/<int:pk>/', security_views.librarian_detail_view, name='librarian_detail'),
    path('register/', security_views.register_view, name='register'),
    path('admin-view/', security_views.admin_view, name='admin_view'),
    path('librarian-view/', security_views.librarian_view, name='librarian_view'),
    path('member-view/', security_views.member_view, name='member_view'),
    path('book-edit/<int:pk>/', security_views.book_edit_view, name='book_edit'),
    path('book-delete/<int:pk>/', security_views.book_delete_view, name='book_delete'),

    # Django's authentication URLs (often included)
    path('accounts/', include('django.contrib.auth.urls')), # Provides login, logout, password reset, etc.
]