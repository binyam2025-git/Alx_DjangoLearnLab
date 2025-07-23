# C:\Users\user\Alx_DjangoLearnLab\advanced_features_and_security\LibraryProject\LibraryProject\urls.py

from django.contrib import admin
from django.urls import path, include
from relationship_app import views as app_views # Changed alias from security_views to app_views for clarity

urlpatterns = [
    path('admin/', admin.site.urls),

    # Your security demo paths (if still needed, adjust as per your project's security demos)
    path('my-form/', app_views.my_form_view, name='my_form'),
    path('my-form-unsafe/', app_views.my_form_unsafe_view, name='my_form_unsafe'),
    path('xss-demo/', app_views.xss_demo_view, name='xss_demo'),

    # Book-related paths with new view names:
    path('books/', app_views.list_books, name='list_books'),
    path('books/add/', app_views.book_add_view, name='add_book'), # Use the new view function name
    path('books/add/success/', app_views.add_book_success, name='add_book_success'),
    path('books/<int:pk>/edit/', app_views.book_edit_view, name='book_edit'),
    path('books/<int:pk>/delete/', app_views.book_delete_view, name='book_delete'),

    # Core app views
    path('', app_views.home_view, name='home'),
    path('authors/', app_views.author_list_view, name='author_list'),
    path('authors/<int:pk>/', app_views.AuthorDetailView.as_view(), name='author_detail'),
    path('libraries/', app_views.library_list_view, name='library_list'),
    path('libraries/<int:pk>/', app_views.LibraryDetailView.as_view(), name='library_detail'),
    path('librarians/<int:pk>/', app_views.librarian_detail_view, name='librarian_detail'),
    path('register/', app_views.register_view, name='register'),
    path('admin-view/', app_views.admin_view, name='admin_view'),
    path('librarian-view/', app_views.librarian_view, name='librarian_view'),
    path('member-view/', app_views.member_view, name='member_view'),

    # Django's authentication URLs
    path('accounts/', include('django.contrib.auth.urls')),
]