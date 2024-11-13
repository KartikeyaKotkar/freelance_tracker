# urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include('clients.urls')),  # Clients app URL routing
    path('projects/', include('projects.urls')),  # Projects app URL routing
    path('invoices/', include('invoices.urls')),  # Invoices app URL routing
]
