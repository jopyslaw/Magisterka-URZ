from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    x = 1 / 0
    return HttpResponse("Hello, World!")