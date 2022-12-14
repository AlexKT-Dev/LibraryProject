from django import forms
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'
