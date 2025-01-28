from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(forms.Form):
    cedula = forms.CharField(max_length=20, label="Cédula")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

    def clean(self):
        cedula = self.cleaned_data.get('cedula')
        password = self.cleaned_data.get('password')
        if cedula and password:
            self.user_cache = authenticate(cedula=cedula, password=password)
            if self.user_cache is None:
                raise forms.ValidationError("Cédula o contraseña incorrectos.")
        return self.cleaned_data

    def get_user(self):
        return self.user_cache