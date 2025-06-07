# Django Vulnerable App

To repozytorium zawiera celowo podatną aplikację Django stworzoną do celów edukacyjnych i testowania narzędzi bezpieczeństwa. Aplikacja zawiera przykłady popularnych podatności spotykanych w aplikacjach webowych.

> **UWAGA:** Aplikacja zawiera realne podatności — uruchamiaj wyłącznie w izolowanym środowisku. Nie wystawiaj jej do internetu ani nie używaj na produkcji.

---

## Przygotowane przykłady podatności

- A01-2021/IDOR
- A01-2021/LFI
- A02-2021/Timing-Attack
- A02-2021/Weak-Encoding-For-Password
- A03-2021/CSRF
- A03-2021/RCE
- A03-2021/SQLI
- A03-2021/XSS
- A04-2021/Login-rate-limit
- A04-2021/Open-Redirect
- A05-2021/Clickjacking
- A05-2021/Debug-mode
- A06-2021/Improperly-Controlled-Modification-of-Dynamically-Determined-Object-Attributes
- A07-2021/Improper-check-for-unusual-or-exceptional-conditions
- A08-2021/Insufficient-Verification-of-Data-Authenticity
- A09-2021/Logging-enable
- A09-2021/Password-in-log
- A10-2021/SSRF

> **UWAGA:** Każda wyżej wymieniona podatność znajduje się na osobnej gałęzi w repozytorium. Nazwa gałezi ma taką samą nazwę jak wyżej wymienione podatności
---

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
git checkout 'nazwa_gałęzi'
```

Przełączyć się na odpowieni branch, który zawiera interesujący nas przykład.

Ostatnim krokiem jest zbudowanie kontenera z aplikacją, za pomocą komendy:

```bash
docker compose up --build
```

Aplikacja po zbudowaniu jest dostępna pod adresem:

```bash
http://localhost:8000
```
