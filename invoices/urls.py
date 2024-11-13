from django.urls import path
from . import views
urlpatterns = [
    path('', views.invoice_list, name='invoice_list'),
    path('invoice/<int:pk>/', views.invoice_detail, name='invoice_detail'),
    path('invoice/new/', views.invoice_create, name='invoice_create'),
    path('invoice/<int:pk>/edit/', views.invoice_edit, name='invoice_edit'),
    path('invoice/<int:pk>/delete/', views.invoice_delete, name='invoice_delete'),
    path('invoice/<int:pk>/mark_paid/', views.invoice_mark_paid, name='invoice_mark_paid'),
]
