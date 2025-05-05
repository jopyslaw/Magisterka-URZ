from django.urls import path
from .views import login_view_unsecure, login_view_secure, home

urlpatterns = [
    path('login-unsecure/', login_view_unsecure),
    path('login-secure/', login_view_secure),
    path('home/', home),
]