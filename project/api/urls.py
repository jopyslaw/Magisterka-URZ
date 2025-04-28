from django.urls import path
from .views import change_notifications

urlpatterns = [
    path('change-notifications/', change_notifications),

]