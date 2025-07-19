# LibraryProject/LibraryProject/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView # Keep this if you have a home.html

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('bookshelf/', include('bookshelf.urls')),
    path('relationships/', include('practice_relationships.urls')),
    path('relationships_app/', include('relationship_app.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # Corrected line   
]