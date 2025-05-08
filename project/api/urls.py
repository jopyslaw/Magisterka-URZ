from django.urls import path
from .views import home, test

urlpatterns = [
    path('profile/', home),
    path('test/', test)
]