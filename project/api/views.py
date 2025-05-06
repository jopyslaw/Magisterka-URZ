from django.http import HttpResponseBadRequest, HttpResponse
from django.contrib.auth.models import User
from django.core import signing
from django.shortcuts import redirect
from django.urls import reverse 


# Create your views here.
def special_offer_vulnerable_no_check(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        return HttpResponse(f"Witaj, {user.username}! Twoja specjalna oferta jest gotowa!")
    except User.DoesNotExist:
        return HttpResponseBadRequest("Nieprawidłowy użytkownik.")
    
def special_offer_corrected_check(request, signed_data_string):
    try:
        data = signing.loads(signed_data_string, max_age=60*60*24*7) 

        if not isinstance(data, dict) or 'user_id' not in data:
             return HttpResponseBadRequest("Nieprawidłowy format danych w linku.")

        user_id = data['user_id']

        try:
            user = User.objects.get(id=user_id)

            return HttpResponse(f"Witaj, {user.username}! Twoja specjalna oferta jest gotowa! (Link ważny)")

        except User.DoesNotExist:
             return HttpResponseBadRequest("Nieprawidłowy użytkownik.")

    except signing.BadSignature:
        return HttpResponseBadRequest("Nieprawidłowy lub sfałszowany link.")
    except signing.SignatureExpired:
        return HttpResponseBadRequest("Link wygasł.")
    except Exception:
         return HttpResponseBadRequest("Wystąpił błąd podczas przetwarzania linku.")
    
def generate_safe_offer_absolute_link_check(request):
    data_to_sign = {'user_id': request.user.id}

    signed_data_string = signing.dumps(data_to_sign, compress=True) 

    relative_url = reverse('api_offer_check', args=[signed_data_string])

    absolute_url = request.build_absolute_uri(relative_url)

    return redirect(absolute_url)