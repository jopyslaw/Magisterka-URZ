from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.conf import settings
import os
import re

# Create your views here.
def get_file_insecure(request):
    if request.method == "GET":
        filename = request.GET.get('filename')

        if filename == None or filename == '':
            return JsonResponse({"error": "Missing required parameter called filename."}, status=400)
        
        file_path = os.path.join(settings.BASE_DIR, 'files', filename)
        try:
            with open(file_path, 'r') as file:
                data = file.read()
        except FileNotFoundError:
            return JsonResponse({"error": "File not exist"}, status=404)
        
        return HttpResponse(data)


def get_file_secure(request):
    if request.method == "GET":
        filename = request.GET.get('filename')

        if filename == None or filename == '':
            return JsonResponse({"error": "Missing required parameter called filename."}, status=400)
        
        if not re.match(r'^[\\w.]+$', filename) or '..' in filename or filename.startswith('/'):
            return JsonResponse({"error": "Invalid filename."}, status=400)

        file_path = os.path.join(settings.BASE_DIR, 'files', filename)

        if not os.path.realpath(file_path).startswith(settings.BASE_DIR + '/files'):
            return JsonResponse({"error": "File not found."}, status=404)

        try:
            with open(file_path, 'r') as file:
                data = file.read()
        except FileNotFoundError:
            return JsonResponse({"error": "File not exist"}, status=404)
        
        return HttpResponse(data)
