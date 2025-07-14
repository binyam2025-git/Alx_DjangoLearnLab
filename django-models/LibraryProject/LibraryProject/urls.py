# LibraryProject/LibraryProject/urls.py
# This is the MAIN project-level URL configuration

from django.contrib import admin
from django.urls import path, include # <--- Make sure 'include' is here

urlpatterns = [
    path('admin/', admin.site.urls), # Standard Django admin URL
    path('relationship_app/', include('relationship_app.urls')), # <--- THIS IS THE CRUCIAL LINE for your app
    # If you have a 'bookshelf' app and its urls.py, you would also include it here, e.g.:
    # path('bookshelf/', include('bookshelf.urls')),
]