from django.urls import path
from . import views # Import views from the current app

app_name = 'relationship_app' # Namespace for URLs, good practice

urlpatterns = [
    # URL for the function-based view (lists all books)
    path('books/', views.book_list, name='book_list'),

    # URL for the class-based view (library detail)
    # <int:pk> captures the primary key (ID) of the library from the URL
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]