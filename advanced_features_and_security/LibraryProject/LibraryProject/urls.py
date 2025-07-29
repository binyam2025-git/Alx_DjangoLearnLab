# C:\Users\user\Alx_DjangoLearnLab\advanced_features_and_security\LibraryProject\LibraryProject\urls.py

from django.contrib import admin
from django.urls import path, include

# IMPORTANT: Import settings for MEDIA_URL and MEDIA_ROOT
from django.conf import settings
# IMPORTANT: Import static for serving media/static files in development
from django.conf.urls.static import static
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # ==============================================================================
    # Include bookshelf app's API URLs
    # This means any request starting with 'api/' will be handled by bookshelf/urls.py
    # ==============================================================================
    path('api/', include('bookshelf.urls')),
    path('api-token-auth/', views.obtain_auth_token),

    # ==============================================================================
    # Include bookshelf app's regular (non-API) URLs
    # This means any request starting with 'books/' will be handled by bookshelf/urls.py
    # This is for your traditional Django views related to books (list, add, edit, delete, form_example)
    # ==============================================================================
    path('books/', include('bookshelf.urls')),

    # ==============================================================================
    # Include relationship_app's URLs
    # This assumes relationship_app handles the root URL ('') and other core paths
    # like authors, libraries, security demos, user management, etc.
    # ==============================================================================
    path('', include('relationship_app.urls')),

    # ==============================================================================
    # Django's built-in authentication URLs (for login, logout, password reset, etc.)
    # ==============================================================================
    path('accounts/', include('django.contrib.auth.urls')),
]

# This block MUST come AFTER urlpatterns is defined.
# It's used during development to serve static and media files.
# In production, a dedicated web server (like Nginx or Apache) typically handles this.
if settings.DEBUG:
    # Serve media files (e.g., uploaded images)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Optional: Serve static files (e.g., CSS, JS, images) if not handled by collectstatic/web server
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)