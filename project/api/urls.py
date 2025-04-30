from django.urls import path
from .views import unsafe_deserialize, safe_deserialize

urlpatterns = [
    path('unsafe-deserialize/', unsafe_deserialize),
    path('safe-deserialize/', safe_deserialize)
]