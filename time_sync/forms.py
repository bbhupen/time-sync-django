from django import forms    
from .models import Participant

passwordInputWidget = {
    'password': forms.PasswordInput(),
}

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'
        widgets = [passwordInputWidget]

class LoginForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['username', 'password']
        widgets = [passwordInputWidget]