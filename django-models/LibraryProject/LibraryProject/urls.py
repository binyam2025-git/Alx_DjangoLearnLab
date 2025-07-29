# LibraryProject/LibraryProject/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView # Keep this if you have a home.html
from relationship_app import views as security_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('bookshelf/', include('bookshelf.urls')),
    path('relationships/', include('practice_relationships.urls')),
    path('relationships_app/', include('relationship_app.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # Corrected line  
   
    path('my-form/', security_views.my_form_view, name='my_form'),
    path('my-form-unsafe/', security_views.my_form_unsafe_view, name='my_form_unsafe'),
    path('xss-demo/', security_views.xss_demo_view, name='xss_demo'),
    path('add-book/', security_views.add_book_view, name='add_book'),
    path('add-book-success/', security_views.add_book_success, name='add_book_success'), 
    path('books/', security_views.list_books, name='list_books'),
    path('', security_views.home_view, name='home'), 
]