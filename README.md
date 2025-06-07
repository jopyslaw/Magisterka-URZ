# A01-2021/LFI

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
git checkout 'A01-2021/LFI'
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

Następnie przejść pod adres 
```bash
http://localhost:8000/api/get-file-insecure?filename=../backend/settings.py
```

Na stronie zostanie wyświetlona zawartość pliku settings.py

## Wersja zabezpieczona

Następnie przejść pod adres 
```bash
http://localhost:8000/api/get-file-secure?filename=../backend/settings.py
```

Na stronie zostanie zwrócony bład "Invalid filename".
