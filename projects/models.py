from django.db import models
from clients.models import Client


class Project(models.Model):
    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')
    start_date = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    completed_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Project: {self.title} for {self.client.name}"

    def mark_completed(self):
        self.status = 'completed'
        self.completed_date = models.DateField(auto_now=True)
        self.save()
