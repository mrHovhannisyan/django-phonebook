from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from phonebook.forms import ContactForm
from phonebook.models import Contact


@login_required
def index(request):
    user = request.user
    contact_name = request.GET.get('contact_name')

    contacts_queryset = Contact.objects.filter(user=user).order_by('first_name')

    # search code
    if contact_name != '' and contact_name is not None:
        contacts = contacts_queryset.filter(first_name__icontains=contact_name).all()
    else:
        contacts = contacts_queryset.all()

    return render(request, 'phonebook/index.html', context={'contacts': contacts})


@login_required
def detail(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)

    return render(request, 'phonebook/detail.html', context={'contact': contact})


@login_required
def create_contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.save(commit=False)
        form.instance.user = request.user
        form.save()
        return redirect('phonebook:index')

    return render(request, 'phonebook/contact_form.html', {'form': form})


@login_required
def update_contact(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    form = ContactForm(request.POST or None, instance=contact)

    if form.is_valid():
        form.save(commit=False)
        form.instance.user = request.user
        form.save()
        return redirect('phonebook:index')

    return render(request, 'phonebook/contact_form.html', {'form': form})


@login_required
def delete_contact(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)

    if request.method == 'POST':
        contact.delete()
        return redirect('phonebook:index')

    return render(request, 'phonebook/delete.html', context={'contact': contact})
