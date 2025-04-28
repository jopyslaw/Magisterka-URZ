from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@csrf_exempt
def change_notifications(request):
    if request.method == "POST":
        notification_status = request.POST.get('notifications', 'off')
        return HttpResponse(f"<h1>Powiadomienia zostały {'włączone' if notification_status == 'on' else 'wyłączone'}!</h1>")
    
    return HttpResponse('''
        <html>
            <head>
                <title>Zmiana ustawienia powiadomień</title>
            </head>
            <body>
                <form method="POST" action="/api/change-notifications/">
                    <button type="submit" name="notifications" value="off" style="width:300px; height:100px;">Wyłącz powiadomienia</button>
                    <button type="submit" name="notifications" value="on" style="width:300px; height:100px;">Włącz powiadomienia</button>
                </form>
            </body>
        </html>
    ''')
