import pickle
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt 
def unsafe_deserialize(request):
    if request.method == 'POST':
        try:
            encoded_data = request.body
            deserialized_data = pickle.loads(encoded_data)
            
            return HttpResponse("Dane zdeserializowane!")
        except Exception as e:
            print(e)
            return HttpResponse(f"Błąd: {str(e)}", status=500)
    return HttpResponse("Wyślij dane POST")

@csrf_exempt
def safe_deserialize(request):
    if request.method == 'POST':
        json_data = request.body.decode('utf-8')  

        try:
            deserialized_data = json.loads(json_data)
            return HttpResponse("Dane bezpiecznie zdeserializowane")
        except json.JSONDecodeError:
            return HttpResponse("Nieprawidłowe dane JSON", status=400)