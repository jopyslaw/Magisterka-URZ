from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from django.contrib.auth.models import User

# Create your views here.
def get_user_non_protected(request):
    user_id = request.GET.get('user_id', "")

    if user_id is None:  
        return JsonResponse({"error": "Missing user_id parameter"}, status=400)

    query = f"SELECT * FROM auth_user WHERE id = {user_id}"  
    
    with connection.cursor() as cursor:
        cursor.execute(query)  
        users = cursor.fetchall()

    if users:
        return JsonResponse({"users": users})
    return JsonResponse({"error": "User not found"}, status=404)


def get_user_protected(request):
    user_id = request.GET.get('user_id')
    
    if user_id is None:  
        return JsonResponse({"error": "Missing user_id parameter"}, status=400)

    try:
        user = User.objects.get(id=user_id) 
        return JsonResponse({"id": user.id, "username": user.username, "password": user.password})
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)
    except ValueError:
        return JsonResponse({"error": "User Id is not a number"})