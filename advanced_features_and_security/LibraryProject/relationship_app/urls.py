# advanced_features_and_security/relationship_app/urls.py

from django.urls import path
from . import views # Import all views from your relationship_app

# If you use Class-Based Views and want to import them directly for clarity:
from .views import AuthorDetailView, LibraryDetailView # Example

urlpatterns = [
    # ==============================================================================
    # Core app views (these will be at the root level because project urls.py includes '' )
    # e.g., '/' for home, '/authors/', '/libraries/'
    # ==============================================================================
    path('', views.home_view, name='home'),
    path('authors/', views.author_list_view, name='author_list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('libraries/', views.library_list_view, name='library_list'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('librarians/<int:pk>/', views.librarian_detail_view, name='librarian_detail'),
    path('register/', views.register_view, name='register'),
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),

    # ==============================================================================
    # Your security demo paths (also at the root level)
    # e.g., '/my-form/', '/xss-demo/'
    # ==============================================================================
    path('my-form/', views.my_form_view, name='my_form'),
    path('my-form-unsafe/', views.my_form_unsafe_view, name='my_form_unsafe'),
    path('xss-demo/', views.xss_demo_view, name='xss_demo'),
]