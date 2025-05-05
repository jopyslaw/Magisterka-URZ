import logging
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def login_view_unsecure(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            logger.info(f"Login attempt: username={username}, password={password}")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/api/home/')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def login_view_secure(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            logger.info(f"Login attempt: username={username}, password=****") 

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/api/home/')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

@login_required
def home(request):
    return HttpResponse(f"<h1>Welcome, {request.user.username}!</h1><p>You are logged in.</p>")