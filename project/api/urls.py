from django.urls import path
from .views import change_email_non_protected, change_email_protected, csrf_attack_non_protected, csrf_attack_protected

urlpatterns = [
    path("change-email-non-protected/", change_email_non_protected),
    path('change-email-protected/', change_email_protected),
    path("csrf-attack-non-protected/", csrf_attack_non_protected),
    path('csrf-attack-protected/', csrf_attack_protected)
]