from django.shortcuts import render
from .forms import IniciarSesionForm
from .forms import RegisterForm
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.http import HttpResponseRedirect
from .forms import CambioDeImagenForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _

# Create your views here.
def landingpage(request):
    return render(request, 'LandingPage.html')

def logout(request):
    do_logout(request)
    return render(request,'LandingPage.html')

def perfil(request):
    return render(request, 'UserProfile.html')


def login(request):
    if request.method == 'POST':
        login_form = IniciarSesionForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            password = login_form.cleaned_data['password']
            user=authenticate(username=user,password=password)
            if user is not None:
                do_login(request,user)
                return render(request, 'LandingPage.html')
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            name = register_form.cleaned_data['name']
            lastname = register_form.cleaned_data['lastname']
            email = register_form.cleaned_data['email']
            password = register_form.cleaned_data['password']
            try:
                user=User.objects.create_user(username=email, email=email, first_name=name, last_name=lastname, password=password)
            except:
                return render(request, 'LogIn.html')

            usuario  =Usuario(user=user, foto="static/img/turing.jpg")
            usuario.save()
            if user is not None:
                do_login(request,user)
                return render(request, 'SuccesReg.html')
    return render(request, 'LogIn.html')


def cambioImagen(request):
    if request.method == 'POST':
        form = CambioDeImagenForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = Usuario.objects.get(user=request.user)
            usuario.foto = request.FILES['file']
            usuario.save()
            return HttpResponseRedirect('/perfil/')
    else:
        form = CambioDeImagenForm()
    return render(request, 'CambioDeImagen.html', {'form': form})

def cambioContraseña(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, _('¡Se ha actualizado la contraseña correctamente!'))
            return HttpResponseRedirect('/perfil/')
        else:
            messages.error(request, _('Porfavor corrregir el error siguiente.'))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'cambioDeContraseña.html', {
        'form': form
    })