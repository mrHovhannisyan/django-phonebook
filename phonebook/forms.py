from django import forms

from phonebook.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['user_id']
