import logging
from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except Exception as e:
                pass
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


logger = logging.getLogger('api')

from django.db import IntegrityError

def contact_view_safe(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                contact = form.save(commit=False)
                contact.save()
            except IntegrityError as e:
                logger.error("Błąd unikalności przy zapisie kontaktu", exc_info=e)
        else:
            logger.error("Formularz nieprzeszedl walidacji: %s", form.errors)
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


