# A03-2021/SQLI

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
git checkout 'A03-2021/SQLI'
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

## Podatny

Należy wejść pod adres:
```bash
http://localhost:8000/api/get-user-non-protected?user_id=1%20OR%201=1
```

W przeglądarce zostaną wyświetleni wszyscy użytkownicy z bazy danych.

## Zabezpieczony

Należy wejść pod adres:
```bash
http://localhost:8000/api/get-user-protected?user_id=1%20OR%201=1
```

W przeglądarce zamiast danych zostanie zwrócony błąd "User Id is not a number"
