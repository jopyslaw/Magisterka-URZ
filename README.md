# A01-2021/IDOR

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
git checkout 'A01-2021/IDOR'
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

Aby sprawdzić podatność trzeba udać się pod adres: 

```bash
http://localhost:8000/admin
```
Zalogować za pomocą następujących danych:

```bash
login: admin
hasło: admin
```

## Wersja podatna

Następnie przejść pod adres 
```bash
http://localhost:8000/api/unsecure-get-invoice/2/
```

Na stronie zostanie wyświetlona informacja o fakturze użytkownika ,który nie jest obecnie zalogowany co potwierdza występowanie podatności

## Wersja zabezpieczona

Następnie przejść pod adres 
```bash
http://localhost:8000/api/secure-get-invoice/2/
```

Na stronie zostanie zwrócony bład 404, który oznacze ,że element nie został znaleziony dla aktualnie zalogowanego użytkownika
