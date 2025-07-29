# bookshelf/urls.py
from django.urls import path
from . import views

app_name = 'bookshelf' # Make sure you have this for namespacing

urlpatterns = [
    # ... your existing bookshelf paths (e.g., restricted-add-book, permission-demo)
    # Add these new paths:
    path('my-form/', views.my_form_view, name='my_form'),
    path('my-form-unsafe/', views.my_form_view_unsafe, name='my_form_unsafe'),
    path('xss-demo/', views.xss_demo_view, name='xss_demo'),
    path('add-book-validated/', views.book_create_view, name='add_book_validated'), # For later validation task
]