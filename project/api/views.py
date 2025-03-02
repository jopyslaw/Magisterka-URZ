from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt  # Wyłączamy ochronę CSRF

# Create your views here.
@login_required
@csrf_exempt  
def change_email_non_protected(request):
    if request.method == "POST":
        new_email = request.POST.get("email")
        request.user.email = new_email
        request.user.save()
        return HttpResponse(f"Email zmieniony na: {new_email}")
    return render(request, "change_mail_non_protected.html")

@login_required
def change_email_protected(request):
    if request.method == "POST":
        new_email = request.POST.get("email")
        request.user.email = new_email
        request.user.save()
        return HttpResponse(f"Email zmieniony na: {new_email}")
    return render(request, "change_mail_protected.html")

@login_required
def csrf_attack_non_protected(request):
    return render(request, "csrf_attack_non_protected.html")

@login_required
def csrf_attack_protected(request):
    return render(request, "csrf_attack_protected.html")