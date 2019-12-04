from django import forms


class IniciarSesionForm(forms.Form):
    user = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=140)
    lastname = forms.CharField(max_length=140)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(max_length=140)

class CambioDeImagenForm(forms.Form):
    file = forms.ImageField()

class UserForm(forms.Form):
    email = forms.EmailField(widget=forms.HiddenInput(), max_length=140)