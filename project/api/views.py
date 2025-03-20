from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django_ratelimit.decorators import ratelimit

# Create your views here.
@csrf_exempt
def vulnerable_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return HttpResponse("Zalogowano pomyślnie!")
        else:
            return HttpResponse("Nieprawidłowe dane logowania.")
    return render(request, "login.html")

@csrf_exempt
@ratelimit(key='ip', rate='3/m', block=True)
def secured_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return HttpResponse("Zalogowano pomyślnie!")
        else:
            return HttpResponse("Nieprawidłowe dane logowania.")
    return HttpResponse("Strona logowania")