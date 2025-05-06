from django.shortcuts import render
import requests
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET
import ipaddress
import socket
from urllib.parse import urlparse


@require_GET
def fetch_url(request):
    url = request.GET.get('url')
    if not url:
        return JsonResponse({'error': 'No URL provided'}, status=400)
    
    try:
        response = requests.get(url)
        return HttpResponse(response.content, content_type='text/plain')
    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)

ALLOWED_DOMAINS = ['example.com', 'api.example.org']

def is_safe_url(url):
    try:
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname

        if hostname not in ALLOWED_DOMAINS:
            return False

        ip = socket.gethostbyname(hostname)
        ip_obj = ipaddress.ip_address(ip)

        if ip_obj.is_private or ip_obj.is_loopback or ip_obj.is_link_local:
            return False

        return True
    except Exception:
        return False

@require_GET
def fetch_url_safe(request):
    url = request.GET.get('url')
    if not url:
        return JsonResponse({'error': 'No URL provided'}, status=400)
    
    if not is_safe_url(url):
        return JsonResponse({'error': 'URL not allowed'}, status=403)

    try:
        response = requests.get(url, timeout=5)
        return HttpResponse(response.content, content_type='text/plain')
    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)