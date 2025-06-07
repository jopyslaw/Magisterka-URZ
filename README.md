# A05-2021/Debug-mode

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
git checkout 'A05-2021/Debug-mode'
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
http://localhost:8000/api/debug/
```

## Zabezpieczona

Należy otworzyć plik settings.py i zmienić wartość pola:
```python
DEBUG = True
```
na
```python
DEBUG = False
```

Wejść pod adres:
```bash
http://localhost:8000/api/debug/
```
