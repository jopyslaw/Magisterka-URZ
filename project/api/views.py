# Create your views here.
from django.shortcuts import render, HttpResponse
from .components.profile_card import ProfileCardView
import sys

def home(request):
    return render(request, 'home.html')

def test(request):
    print(sys.modules['django'].views.defaults.ERROR_PAGE_TEMPLATE)

    return HttpResponse(sys.modules['django'].views.defaults.ERROR_PAGE_TEMPLATE)
