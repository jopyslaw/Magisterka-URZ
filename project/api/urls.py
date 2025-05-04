from django.urls import path
from django.contrib.auth import views as auth_views
from .views import password_reset_view_secure, password_reset_view_unsecure

urlpatterns = [
    path('reset-password-unsecure/', password_reset_view_unsecure, name='password_reset'),
    path('reset-password-secure/', password_reset_view_secure, name='password_reset'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]