# mywebproject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', include('webapp.urls')),  # Add this line
    path('accounts/', include('accounts.urls')),
    path('', include('webapp.urls')),  # Add this line

]
