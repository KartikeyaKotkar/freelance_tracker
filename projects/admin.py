from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'client', 'status', 'deadline', 'start_date']
    search_fields = ['title', 'client__name']
    list_filter = ['status', 'deadline']
