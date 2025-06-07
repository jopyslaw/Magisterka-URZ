# A02-2021/Timing-Attack

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
git checkout 'A02-2021/Timing-Attack'
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

Należy otworzyć plik settings.py i zakomentować linie w tablicy AUTHENTICATION_BACKENDS o treści:
```bash
"api.authentication.SafeModelBackend",
```
oraz odkomentować linie o treści:
```bash
'django.contrib.auth.backends.ModelBackend',
```
Tak powinna prezentować się tablica AUTHENTICATION_BACKENDS po zmianiach:
```python
AUTHENTICATION_BACKENDS = [
    #"api.authentication.SafeModelBackend", # Własna metoda służąca do autentykacji użytkownika która jest zabezpieczona przed podatnością
    'django.contrib.auth.backends.ModelBackend', # Domyślny backend w którym istnieje podatność
]
```
Następnie przebudować kontener za pomocą komendy:
```bash
docker compose up --build
```
I uruchomić program testowy znajdujący się w folderze testing-tools o nazwie:
```bash
timing-attack-example.py
```
za pomocą komendy:
```bash
python timing-attack-example.py
```

Na ekranie konsoli zostaną wyświetlone wyniki

## Wersja zabezpieczona

Należy otworzyć plik settings.py i zakomentować linie w tablicy AUTHENTICATION_BACKENDS o treści:
```bash
'django.contrib.auth.backends.ModelBackend',
```
oraz odkomentować linie o treści:
```bash
"api.authentication.SafeModelBackend",
```
Tak powinna prezentować się tablica AUTHENTICATION_BACKENDS po zmianiach:
```python
AUTHENTICATION_BACKENDS = [
    "api.authentication.SafeModelBackend", # Własna metoda służąca do autentykacji użytkownika która jest zabezpieczona przed podatnością
    #'django.contrib.auth.backends.ModelBackend', # Domyślny backend w którym istnieje podatność
]
```
Następnie przebudować kontener za pomocą komendy:
```bash
docker compose up --build
```
I uruchomić program testowy znajdujący się w folderze testing-tools o nazwie:
```bash
timing-attack-example.py
```
za pomocą komendy:
```bash
python timing-attack-example.py
```

Na ekranie konsoli zostaną wyświetlone wyniki
