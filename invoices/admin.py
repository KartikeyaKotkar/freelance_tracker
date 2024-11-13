from django.contrib import admin
from .models import Invoice

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['client', 'project', 'amount', 'status', 'due_date', 'issue_date']
    search_fields = ['client__name', 'project__title']
    list_filter = ['status', 'due_date', 'issue_date']
