from django.shortcuts import render, redirect
from django.utils.http import url_has_allowed_host_and_scheme


# Create your views here.
def unsafe_redirect(request):
    if request.method == "GET":
        next_url = request.GET.get('next', '/')
        return redirect(next_url)


def safe_redirect(request):
    if request.method == "GET":
        next_url = request.GET.get('next', '/')
        allowed_hosts = {request.get_host()}
        if url_has_allowed_host_and_scheme(next_url, allowed_hosts=allowed_hosts):
            return redirect(next_url)
        return redirect('/')
    


    