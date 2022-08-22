from django.http import HttpResponse


def phonebook(request):
    return HttpResponse("Hi from phonebook")
