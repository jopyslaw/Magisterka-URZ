# A05-2021/Cookie-no-expire

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
git checkout 'A05-2021/Cookie-no-expire'
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

Należy udać się pod adres:
```bash
http://localhost:8000/api/login
```
i zalogować się za pomocą danych:
```bash
login: admin
hasło: admin
```
Wcisnąć przycisk zaloguj

## Zabezpieczona

Należy otworzyć plik settings.py i zmienić następujące linie:
```python
SESSION_COOKIE_AGE = 2147483647 
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_SECURE = False 
SESSION_COOKIE_HTTPONLY = True  
SESSION_COOKIE_SAMESITE = 'Lax'  
```
na:
```python
SESSION_COOKIE_AGE = 86400 
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True  
SESSION_COOKIE_SAMESITE = 'Strict'  
```

Następnie przebudować kontener za pomocą komendy:
```bash
docker compose up --build
```

i powtórzyć operacje z sekcji 'Podatna'
