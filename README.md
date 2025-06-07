# A07-2021/Improper-check-for-unusual-or-exceptional-conditions

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
git checkout 'A07-2021/Improper-check-for-unusual-or-exceptional-conditions'
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
http://localhost:8000/api/reset-password-unsecure/
```

W wyświetlonym formularzu resetu hasła wpisać następujący adres email:
```bash
test@com.pl
```
Następnie wysłać

## Zabezpieczona

Wejść pod adres:
```bash
http://localhost:8000/api/reset-password-secure/
```

W wyświetlonym formularzu resetu hasła wpisać następujący adres email:
```bash
test@com.pl
```

Następnie wysłać
