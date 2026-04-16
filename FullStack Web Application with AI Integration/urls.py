from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Full stack web application with AI Integration"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),
]