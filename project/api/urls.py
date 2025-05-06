from django.urls import path
from .views import fetch_url, fetch_url_safe

urlpatterns = [
    path('fetch-url-unsafe/', fetch_url),
    path('fetch-url-safe/', fetch_url_safe)
]