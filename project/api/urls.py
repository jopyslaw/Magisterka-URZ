from django.urls import path
from .views import get_file_insecure, get_file_secure

urlpatterns = [
    path('get-file-insecure', get_file_insecure),
    path('get-file-secure', get_file_secure)
]