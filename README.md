# A03-2021/RCE

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
git checkout 'A03-2021/RCE'
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

Aby przetestować aplikację wystarczy uruchomić pomocniczy program który znaduje się w projekcie w folderze tools pod nazwą exploit.py i uruchomić go za pomocą polecenia:

```bash
python exploit.py
```

Zostanie wtedy uruchomione oprogramowanie, które wyśle żądanie pod dwa endpointy, gdzie jeden podatny na atak, a kolejny jest zabezpieczony 
