from django import forms


class IniciarSesionForm(forms.Form):
    user = forms.CharField()
    password = forms.CharField()


class nombrexdForm(forms.Form):
    nombrexd = forms.CharField(label='nombrexd', max_length=100)


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=140)
    lastname = forms.CharField(max_length=140)
    password = forms.CharField(max_length=140)
    email = forms.CharField(max_length=140)
