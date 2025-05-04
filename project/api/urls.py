from django.urls import path
from .views import view_invoice_unsecure, view_invoice_secure

urlpatterns = [
    path("unsecure-get-invoice/<int:invoice_id>/", view_invoice_unsecure),
    path("secure-get-invoice/<int:invoice_id>/", view_invoice_secure)
]