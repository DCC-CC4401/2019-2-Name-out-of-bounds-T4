from django import forms

class IniciarSesionForm(forms.Form):
    user = forms.CharField()
    password = forms.CharField()

class nombrexdForm(forms.Form):
    nombrexd = forms.CharField(label='nombrexd', max_length=100)
