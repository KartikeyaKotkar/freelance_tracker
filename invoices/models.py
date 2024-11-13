from django.db import models
from clients.models import Client
from projects.models import Project


class Invoice(models.Model):
    STATUS_CHOICES = [
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
        ('overdue', 'Overdue'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='unpaid')
    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    paid_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Invoice for {self.client.name} - {self.project.title}"

    def is_overdue(self):
        return self.due_date < datetime.date.today() and self.status != 'paid'

    def mark_paid(self):
        self.status = 'paid'
        self.paid_date = datetime.date.today()
        self.save()
