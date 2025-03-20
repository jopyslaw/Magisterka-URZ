from django.urls import path
from .views import vulnerable_login, secured_login

urlpatterns = [
    path('insecured-login/',vulnerable_login),
    path('secured-login/', secured_login)
]