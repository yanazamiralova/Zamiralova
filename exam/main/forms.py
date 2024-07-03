from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Statement


class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True, help_text='Номер телефона')
    full_name = forms.CharField(max_length=200, required=True, help_text='ФИО')
    city = forms.CharField(max_length=100, required=True, help_text='Город')


    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'phone_number',
            'full_name',
            'city',
            'password1',
            'password2',
        )


class StatementForm(forms.ModelForm):
    class Meta:
        model = Statement
        fields = [
            'numbers',
            'description',
        ]
        widgets = {
            'numbers': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер машины'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
        }