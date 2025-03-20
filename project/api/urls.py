from django.urls import path
from .views import safe_redirect, unsafe_redirect

urlpatterns = [
    path("redirect-non-protected/", unsafe_redirect),
    path("redirect-protected/", safe_redirect)
]