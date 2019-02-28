from django import forms
from .models import Contacts


class NewContactForm(forms.ModelForm):
    class Meta():
        model = Contacts
        fields = '__all__'