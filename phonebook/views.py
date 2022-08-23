from django.http import HttpResponse
from django.shortcuts import render

from phonebook.forms import ContactForm
from phonebook.models import Contact


def index(request):
    contacts = Contact.objects.all()

    return render(request, 'phonebook/index.html', context={'contacts': contacts})


def phonebook(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponse("Hi from phonebook")

    return render(request, 'phonebook/contact_form.html', {'form': form})
