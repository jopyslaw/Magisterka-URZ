from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Invoice

# Create your views here.
def view_invoice_unsecure(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    return HttpResponse(f"Invoice for {invoice.user.username}: {invoice.amount}")

def view_invoice_secure(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id, user=request.user)
    return HttpResponse(f"Invoice for {invoice.user.username}: {invoice.amount}")
