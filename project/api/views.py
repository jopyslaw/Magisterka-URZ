from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            response = HttpResponse(f"Zalogowano jako {user.username}")
            return response
        else:
            return HttpResponse("Błędne dane logowania")
    
    return render(request, 'login.html')