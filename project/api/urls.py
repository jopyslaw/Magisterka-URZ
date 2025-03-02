from django.urls import path
from .views import get_user_non_protected, get_user_protected

urlpatterns = [
    path('get-user-protected', get_user_protected),
    path('get-user-non-protected', get_user_non_protected)
]