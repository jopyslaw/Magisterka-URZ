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
        user = cursor.fetchone()
        print(user)

    if user:
        return JsonResponse({"id": user[0], "username": user[4], "password": user[1]})
    return JsonResponse({"error": "User not found"}, status=404)


def get_user_protected(request):
    user_id = request.GET.get('user_id')
    
    if user_id is None:  
        return JsonResponse({"error": "Missing user_id parameter"}, status=400)

    if not user_id.isdigit():  
        return JsonResponse({"error": "Invalid ID"}, status=400)

    try:
        user = User.objects.get(id=user_id) 
        return JsonResponse({"id": user.id, "username": user.username, "password": user.password})
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)