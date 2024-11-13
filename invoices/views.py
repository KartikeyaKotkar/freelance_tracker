# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Invoice
from .forms import InvoiceForm
from clients.models import Client
from projects.models import Project

# List all invoices
def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'invoices/invoice_list.html', {'invoices': invoices})

# View details of a specific invoice
def invoice_detail(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    return render(request, 'invoices/project_detail.html', {'invoice': invoice})

# Create a new invoice
def invoice_create(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = InvoiceForm()
    return render(request, 'invoices/project_form.html', {'form': form})

# Edit an existing invoice
def invoice_edit(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect('invoice_detail', pk=invoice.pk)
    else:
        form = InvoiceForm(instance=invoice)
    return render(request, 'invoices/project_form.html', {'form': form})

# Delete an invoice
def invoice_delete(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        invoice.delete()
        return redirect('invoice_list')
    return render(request, 'invoices/project_confirm_delete.html', {'invoice': invoice})

# Mark invoice as paid
def invoice_mark_paid(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    invoice.mark_paid()
    return redirect('invoice_detail', pk=invoice.pk)
