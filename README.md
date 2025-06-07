# A09-2021/Password-in-log

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
git checkout 'A09-2021/Password-in-log'
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

Wejść pod adres:
```bash
http://localhost:8000/api/login-unsecure/
```
Wypełnić formularz następującymi danymi:
```bash
login: admin
hasło: admin
```
Wysłać formularz

## Zabezpieczona

Wejść pod adres:
```bash
http://localhost:8000/api/login-unsecure/
```
Wypełnić formularz następującymi danymi:
```bash
login: admin
hasło: admin
```
Wysłać formularz
