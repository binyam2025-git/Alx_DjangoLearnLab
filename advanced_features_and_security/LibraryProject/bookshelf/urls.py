# advanced_features_and_security/bookshelf/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Import your DRF API views (assuming these are defined in bookshelf/views.py)
from .views import BookListCreateAPIView, AuthorListCreateAPIView, BookRetrieveUpdateDestroyAPIView, CommentViewSet

# Import any other regular Django views from bookshelf/views.py
# These would be views that render HTML templates for forms, lists, etc.
from . import views as bookshelf_regular_views # Alias for clarity if needed, or just from . import views

router = DefaultRouter()
# Register your ViewSets with the router
router.register(r'comments', CommentViewSet) # Register CommentViewSet

urlpatterns = [
    # ==============================================================================
    # Django REST Framework API URLs
    # These paths are relative to the '/api/' prefix defined in the project's urls.py
    # So 'api/books/' maps to 'books/' here.
    # ==============================================================================
    # Path for listing and creating books, now with filtering capability
    path("books/", BookListCreateAPIView.as_view(), name="book_list_create"),
    # Optional: Path for listing and creating authors
    path('authors/', AuthorListCreateAPIView.as_view(), name='author-list-create'),
    
    path("books/<int:pk>/", BookRetrieveUpdateDestroyAPIView.as_view(), name="api_book_detail_update_delete"),

    # ==============================================================================
    # Regular Django Views for the 'bookshelf' app
    # These paths are relative to the '/books/' prefix defined in the project's urls.py
    # So '/books/' maps to '' here; '/books/add/' maps to 'add/' here.
    # ==============================================================================
    path('form-example/', bookshelf_regular_views.form_example_view, name='form_example'),
    path('', bookshelf_regular_views.book_list, name='book_list'), # Handles /books/
    path('add/', bookshelf_regular_views.book_add_view, name='add_book'), # Handles /books/add/
    path('add/success/', bookshelf_regular_views.add_book_success, name='add_book_success'), # Handles /books/add/success/
    path('<int:pk>/edit/', bookshelf_regular_views.book_edit_view, name='book_edit'), # Handles /books/<int:pk>/edit/
    path('<int:pk>/delete/', bookshelf_regular_views.book_delete_view, name='book_delete'), # Handles /books/<int:pk>/delete/
    
    # Include the router's URLs under a base path like 'api/'
    path('', include(router.urls)), # This will make URLs like /comments/, /comments/{id}/
]