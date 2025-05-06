from django.urls import path
from .views import special_offer_vulnerable_no_check, special_offer_corrected_check, generate_safe_offer_absolute_link_check

urlpatterns = [
    path('offer-no-check/<int:user_id>/', special_offer_vulnerable_no_check),
    path('offer-check/<str:signed_data_string>/', special_offer_corrected_check, name='api_offer_check'),
    path('offer-check/', generate_safe_offer_absolute_link_check, )
]