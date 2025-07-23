# C:\Users\user\Alx_DjangoLearnLab\advanced_features_and_security\LibraryProject\LibraryProject\urls.py

from django.contrib import admin
from django.urls import path, include
from relationship_app import views as relationship_app_views # Keep this alias for views that stay here
from bookshelf import views as bookshelf_views # NEW: Alias for bookshelf views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Your security demo paths (still point to relationship_app_views)
    path('my-form/', relationship_app_views.my_form_view, name='my_form'),
    path('my-form-unsafe/', relationship_app_views.my_form_unsafe_view, name='my_form_unsafe'),
    path('xss-demo/', relationship_app_views.xss_demo_view, name='xss_demo'),

    # Book-related paths: NOW POINT TO bookshelf_views and update name for book_list
    path('books/', bookshelf_views.book_list, name='book_list'), # UPDATED name and view
    path('books/add/', bookshelf_views.book_add_view, name='add_book'),
    path('books/add/success/', bookshelf_views.add_book_success, name='add_book_success'),
    path('books/<int:pk>/edit/', bookshelf_views.book_edit_view, name='book_edit'),
    path('books/<int:pk>/delete/', bookshelf_views.book_delete_view, name='book_delete'),

    # Core app views (still point to relationship_app_views)
    path('', relationship_app_views.home_view, name='home'),
    path('authors/', relationship_app_views.author_list_view, name='author_list'),
    path('authors/<int:pk>/', relationship_app_views.AuthorDetailView.as_view(), name='author_detail'),
    path('libraries/', relationship_app_views.library_list_view, name='library_list'),
    path('libraries/<int:pk>/', relationship_app_views.LibraryDetailView.as_view(), name='library_detail'),
    path('librarians/<int:pk>/', relationship_app_views.librarian_detail_view, name='librarian_detail'),
    path('register/', relationship_app_views.register_view, name='register'),
    path('admin-view/', relationship_app_views.admin_view, name='admin_view'),
    path('librarian-view/', relationship_app_views.librarian_view, name='librarian_view'),
    path('member-view/', relationship_app_views.member_view, name='member_view'),

    # Django's authentication URLs
    path('accounts/', include('django.contrib.auth.urls')),
]