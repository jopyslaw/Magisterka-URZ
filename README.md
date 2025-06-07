# A04-2021/Open-Redirect

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
git checkout 'A04-2021/Open-Redirect'
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

Należy wejść pod adres:
```bash
http://localhost:8000/api/redirect-non-protected?next=https://jopyslaw.github.io/my-site/
```

Nastąpi przekierowanie na stronę https://jopyslaw.github.io/my-site/.

## Zabezpieczona

Należy wejść pod adres:
```bash
http://localhost:8000/api/redirect-protected?next=https://jopyslaw.github.io/my-site/
```

Przekierowanie nie następuje.
