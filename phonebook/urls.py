from django.urls import path

from phonebook import views

app_name = 'phonebook'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contact_id>', views.detail, name='detail'),
    path('add', views.create_contact, name='create_contact'),
    path('update/<int:contact_id>', views.update_contact, name='update_contact'),
    path('delete/<int:contact_id>', views.delete_contact, name='delete_contact'),
]
