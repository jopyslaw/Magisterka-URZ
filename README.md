# A08-2021/Insufficient-Verification-of-Data-Authenticity

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
git checkout 'A08-2021/Insufficient-Verification-of-Data-Authenticity'
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

## Podatna

Wejść pod adres:
```bash
http://localhost:8000/api/offer-no-check/1/
```

Zostanie wyświetlona oferta dla użytkownika o id 1, a jeśli zostanie zmienione id to oferta zostanie wyświetlona dla użytkownika o podanym id 

## Zabezpieczona

Wejść pod adres:
```bash
http://localhost:8000/api/offer-check/
```

Zostanie wyświetlona oferta dla użytkownika o danym id
