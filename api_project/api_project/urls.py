
# ~/Alx_DjangoLearnLab/api_project/api_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')), # This line should now correctly resolve
]
