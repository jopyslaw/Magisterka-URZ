# A02-2021/Weak-Encoding-For-Password

## Uruchomienie

Aby uruchomić aplikację lokalnie za pomocą Dockera, najpierw musimy pobrać repozytorium za pomocą polecenia:

```bash
git clone https://github.com/jopyslaw/Magisterka-URZ
```
Kolejnym krokiem jest wejście do pobranego repozytorium, używając komendy:

```bash
cd Magister-URZ
```

Następnie za pomocą komendy

```git
git checkout 'A02-2021/Weak-Encoding-For-Password'
```

Przełączyć się na odpowieni branch, który zawiera opisywany przykład.

Ostatnim krokiem jest zbudowanie kontenera za pomocą komendy:

```bash
docker compose up --build
```

Aplikacja po zbudowaniu jest dostępna pod adresem:

```bash
http://localhost:8000
```

## Wersja podatna

Należy otworzyć plik settings.py i zakomentować linie w tablicy PASSWORD_HASHERS o treści:
```bash
'django.contrib.auth.hashers.MD5PasswordHasher', # Hasher MD5 który jest obecnie jednym z najgorszych algorytmów służących do hashowania
'django.contrib.auth.hashers.Argon2PasswordHasher', # Argon2 Hasher jeden z najlepszych hasherów obecnie dostępnych
'django.contrib.auth.hashers.PBKDF2PasswordHasher',
```
oraz odkomentować linie o treści:
```bash
'api.hashers.PlaintextPasswordHasher', # Autorski hasher który nie hashuje hasła tylko zapiusje jest jako zwykły tekst

```
Tak powinna prezentować się tablica AUTHENTICATION_BACKENDS po zmianiach:
```python
PASSWORD_HASHERS = [
    'api.hashers.PlaintextPasswordHasher', # Autorski hasher który nie hashuje hasła tylko zapiusje jest jako zwykły tekst
    #'django.contrib.auth.hashers.MD5PasswordHasher', # Hasher MD5 który jest obecnie jednym z najgorszych algorytmów służących do hashowania
    #'django.contrib.auth.hashers.Argon2PasswordHasher', # Argon2 Hasher jeden z najlepszych hasherów obecnie dostępnych
    #'django.contrib.auth.hashers.PBKDF2PasswordHasher',
]
]
```
Następnie przebudować kontener za pomocą komendy:
```bash
docker compose up --build
```

Dodanie nowego użytkownika, bedzie skutkowało zapisaniem jego hasła w bazie danych w formie tekstu.

## Wersja zabezpieczona

Należy otworzyć plik settings.py i zakomentować linie w tablicy AUTHENTICATION_BACKENDS o treści:
```bash
'api.hashers.PlaintextPasswordHasher', # Autorski hasher który nie hashuje hasła tylko zapiusje jest jako zwykły tekst
'django.contrib.auth.hashers.MD5PasswordHasher', # Hasher MD5 który jest obecnie jednym z najgorszych algorytmów służących do hashowania
'django.contrib.auth.hashers.Argon2PasswordHasher', # Argon2 Hasher jeden z najlepszych hasherów obecnie dostępnych
```
oraz odkomentować linie o treści:
```bash
#'django.contrib.auth.hashers.PBKDF2PasswordHasher',
```
Tak powinna prezentować się tablica AUTHENTICATION_BACKENDS po zmianiach:
```python
PASSWORD_HASHERS = [
    #'api.hashers.PlaintextPasswordHasher', # Autorski hasher który nie hashuje hasła tylko zapiusje jest jako zwykły tekst
    #'django.contrib.auth.hashers.MD5PasswordHasher', # Hasher MD5 który jest obecnie jednym z najgorszych algorytmów służących do hashowania
    #'django.contrib.auth.hashers.Argon2PasswordHasher', # Argon2 Hasher jeden z najlepszych hasherów obecnie dostępnych
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
]

```
Następnie przebudować kontener za pomocą komendy:
```bash
docker compose up --build
```

Dodanie nowego użytkownika, bedzie skutkowało zapisaniem jego hasła w bazie danych w formie zaszyfrowanej.
