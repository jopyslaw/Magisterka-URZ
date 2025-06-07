# A05-2021/Clickjacking

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
git checkout 'A05-2021/Clickjacking'
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

## Podatna

Należy otworzyć plik settings.py i zakomentować linie w tablicy MIDDLEWARE o treści:
```bash
#'django.middleware.clickjacking.XFrameOptionsMiddleware',
```

Tak powinna prezentować się tablica AUTHENTICATION_BACKENDS po zmianiach:
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```
Następnie przebudować kontener za pomocą komendy:
```bash
docker compose up --build
```

Wejść w folder api/templates i uruchomić plik HTML o nazwie:
```bash
clickjacking_attack.html
```
za pomocą przeglądarki. Po wyświetleniu strony wystarczy wcisnąć przycisk "Kliknij, aby odebrać prezent!"


## Zabezpieczona

Należy otworzyć plik settings.py i odkomentować linie w tablicy MIDDLEWARE o treści:
```bash
#'django.middleware.clickjacking.XFrameOptionsMiddleware',
```

Tak powinna prezentować się tablica AUTHENTICATION_BACKENDS po zmianiach:
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```
Następnie przebudować kontener za pomocą komendy:
```bash
docker compose up --build
```

Wejść w folder api/templates i uruchomić plik HTML o nazwie:
```bash
clickjacking_attack.html
```
za pomocą przeglądarki. Po wyświetleniu strony wystarczy wcisnąć przycisk "Kliknij, aby odebrać prezent!". 
