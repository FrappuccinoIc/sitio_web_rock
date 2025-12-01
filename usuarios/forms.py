from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label = "Nombre de usuario", required = True, max_length=50, min_length=3)
    password = forms.CharField(label = "Contraseña", required = True, widget=forms.PasswordInput, min_length=8, max_length=24)
    confirm_password = forms.CharField(label = "Confirmar Contraseña", required = True, widget=forms.PasswordInput, min_length=8, max_length=24)