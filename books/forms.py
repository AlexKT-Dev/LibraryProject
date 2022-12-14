from django import forms
from .models import *


class BooksForm(forms.ModelForm):
    class Meta:
        model = BooksModel
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'user': forms.Select(attrs={'class': 'form-select'}),
            'pub_date': forms.DateInput(attrs={'class': 'form-control'}),
            'is_pub': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
