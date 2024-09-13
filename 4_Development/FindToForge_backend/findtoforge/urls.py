# Main/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authSystem_app.urls')),
    path('', include('Main_app.urls')),
]
