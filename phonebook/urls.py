from django.urls import path

from phonebook import views

app_name = 'phonebook'
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.phonebook, name='create_contact'),
]
