from django import forms    
from .models import Participant
from django.forms import TextInput, EmailInput, PasswordInput

passwordInputWidget = {
    'password': forms.PasswordInput(attrs={'type': 'password'})
}

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control mb-3',
            }),
            'email': EmailInput(attrs={
                'class': 'form-control mb-3',
            }),
            'password': PasswordInput(attrs={
                'class': 'form-control mb-3',
            })
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['username', 'password']
        widgets = widgets = {
            'username': TextInput(attrs={
                'class': 'form-control mb-3',
            }),
            'password': PasswordInput(attrs={
                'class': 'form-control mb-3',
            })
        }