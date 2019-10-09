from django.shortcuts import render
from .forms import IniciarSesionForm
from .forms import RegisterForm
from .models import *


# Create your views here.
def landingpage(request):
    return render(request, 'LandingPage.html')


def perfil(request):
    return render(request, 'UserProfile.html')


def login(request):
    if request.method == 'POST':
        login_form = IniciarSesionForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            password = login_form.cleaned_data['password']
            return render(request, 'LogIn.html', {'nombrexd': user, 'resultados': password})

    else:
        login_form = IniciarSesionForm()
        print("jajaj ayuda")
        return render(request, 'LogIn.html', {'resultados': "what"})


def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            name = register_form.cleaned_data['name']
            lastname = register_form.cleaned_data['lastname']
            email = register_form.cleaned_data['email']
            password = register_form.cleaned_data['password']
            emlen = len(email)
            user = User.objects.create_user(username=email, email=email, first_name=name, last_name=lastname,
                                            password=password)
            user.save()
            email = email[0:3] + "****" + email[emlen - 7:emlen]

            return render(request, 'SuccesReg.html', {'nombre': (name + " " + lastname), 'mail': email})
    else:
        return render(request, 'Register.html')
