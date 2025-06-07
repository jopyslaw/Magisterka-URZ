# A04-2021/Login-rate-limit

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
git checkout 'A04-2021/Login-rate-limit'
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

Aby przetestować podatność wystarczy uruchomić program pomocniczny który znaduje się w folderze additional-tool razem z projektem, za pomocą komendy:
```bash
python bruteforcelogin.py
```

Program wykonuje prosty atak słownikowy, do złamania hasła dla użytkownika admin. Wysyła żądania do dwóch endpointów jeden który nie posiada mechanizmu rate-limitu i jeden który go posiada. Wyniki pokazują się w konosli wraz z działaniem programu.
