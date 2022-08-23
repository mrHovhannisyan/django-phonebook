from django.http import HttpResponse
from django.shortcuts import render, redirect

from phonebook.forms import ContactForm
from phonebook.models import Contact


def index(request):
    contacts = Contact.objects.all()

    return render(request, 'phonebook/index.html', context={'contacts': contacts})


def detail(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)

    return render(request, 'phonebook/detail.html', context={'contact': contact})


def create_contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('phonebook:index')

    return render(request, 'phonebook/contact_form.html', {'form': form})


def update_contact(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    form = ContactForm(request.POST or None, instance=contact)

    if form.is_valid():
        form.save()
        return redirect('phonebook:index')

    return render(request, 'phonebook/contact_form.html', {'form': form})
