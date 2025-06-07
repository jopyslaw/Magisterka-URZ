# A03-2021/XSS

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
git checkout 'A03-2021/XSS'
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
http://127.0.0.1:8000/api/comment-unsecured/?comment=<script>alert('XSS!');</script>
```

Po przejściu pod adres powinno wyświetlić się okno z napisem "XSS!"

## Zabezpieczony

Należy wejść pod adres:
```bash
http://127.0.0.1:8000/api/comment-secured/?comment=<script>alert('XSS!');</script>
```

W przeglądarce powinien wyświetlić się napis "<script>alert('XSS!');</script>"
