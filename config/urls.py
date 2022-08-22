from django.contrib import admin
from django.urls import path

from phonebook.views import phonebook

urlpatterns = [
    path('admin/', admin.site.urls),
    path('phonebook/', phonebook, name='phonebook'),
]
