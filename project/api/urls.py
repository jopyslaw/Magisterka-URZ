from django.urls import path
from .views import contact_view, contact_view_safe

urlpatterns = [
    path('contact-unsafe/', contact_view),
    path('contact-safe/', contact_view_safe)
]