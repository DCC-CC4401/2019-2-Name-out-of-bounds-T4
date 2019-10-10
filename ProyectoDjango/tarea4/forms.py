from django import forms
from .models import *

class IniciarSesionForm(forms.Form):
    user = forms.CharField()
    password = forms.CharField()

class ImageForm(forms.Form):
    imagefile = forms.ImageField()