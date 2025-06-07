# A03-2021/CSRF

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
git checkout 'A03-2021/CSRF'
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
login: test
hasło: zaq1@WSX
```

## Wersja podatna

Następnie przejść pod adres 
```bash
http://localhost:8000/api/csrf-attack-non-protected/
```

Atak zostaje wykonany i adres e-mail aktualnie zalogowanego użytkownika zostaje zmieniony

## Wersja zabezpieczona

Następnie przejść pod adres 
```bash
http://localhost:8000/api/csrf-attack-protected/
```

Atak zostaje powstrzymany i nie dochodzi do zmiany adresu e-mail zalogowanego użytkownika
