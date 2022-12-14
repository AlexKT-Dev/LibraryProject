from django import forms
from .models import *


class BooksForm(forms.ModelForm):
    class Meta:
        model = BooksModel
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
        }
