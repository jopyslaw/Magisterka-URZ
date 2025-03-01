import requests
import timeit

URL = "http://127.0.0.1:8000/api/login/"  
TEST_USER = "konrad2"  
BAD_USER = "test"  
NOT_EXIST_USER = "nieistniejacy user"

def measure_response_time(url,username):
    """Mierzy czas odpowiedzi serwera na próbę logowania"""
    data = {"username": username, "password": "haslo"}
    start = timeit.default_timer()
    requests.post(url, data=data)
    return timeit.default_timer() - start

real_user_time = measure_response_time(URL,TEST_USER)
fake_user_time = measure_response_time(URL,BAD_USER)
not_exist_user_time = measure_response_time(URL,NOT_EXIST_USER)
print(f"Czas odpowiedzi dla użytkownika bez ustawionego hasła: {real_user_time:.6f} s")
print(f"Czas odpowiedzi dla użytkownika z ustawionym hasłem: {fake_user_time:.6f} s")
print(f"Czas odpowiedzi dla nieistniejącego użytkownika: {not_exist_user_time:.6f} s")

if fake_user_time > real_user_time:
    print("💥 Można wykryć, czy użytkownik istnieje! System podatny na atak timingowy.")
else:
    print("✅ System bezpieczny.")