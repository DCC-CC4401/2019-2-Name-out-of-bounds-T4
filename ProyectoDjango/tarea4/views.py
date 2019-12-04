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
from django.utils.translation import ugettext as _
from django.db.models import Q
from .forms import UserForm


# Create your views here.
def landingpage(request):
    return render(request, 'LandingPage.html')


def logout(request):
    do_logout(request)
    return render(request, 'LandingPageNoLoggeados.html')


def perfil(request):

    if 'q' in request.GET:
        query = request.GET.get('q')
        busqueda = Usuario.objects.filter(
            Q(user__first_name__icontains=query) | Q(user__last_name__icontains=query)
        ).exclude(user=request.user)

        for u in busqueda:

            try:
                usr = Usuario.objects.get(user=request.user)
                Relaciones.objects.get(user_1=u, user_2=usr)
                Relaciones.objects.get(user_1=usr, user_2=u)
                busqueda = busqueda.exclude(user=u.user)

            except Relaciones.DoesNotExist:
                pass
    else:
        busqueda = []

    if 'agregar_amigo' in request.POST:

        amigo_form = UserForm(request.POST)

        if amigo_form.is_valid():

            amigo = amigo_form.cleaned_data['email']
            add = Usuario.objects.get(user__email=amigo)
            adder = Usuario.objects.get(user=request.user)
            relacion1 = Relaciones(user_1=adder,user_2=add, estado='1') # 1 manda la solicitud
            relacion2 = Relaciones(user_1=add, user_2=adder, estado='2') # 1 recibe la solicitud
            relacion1.save()
            relacion2.save()

        else:
            print("wtf")

    elif 'aceptar_sol' in request.POST:
        amigo_form = UserForm(request.POST)
        if amigo_form.is_valid():
            amigo = amigo_form.cleaned_data['email']
            amigo_usuario = Usuario.objects.get(user__email=amigo)
            usuario = Usuario.objects.get(user=request.user)
            rel1 = Relaciones.objects.get(user_1=amigo_usuario, user_2=usuario, estado='1')
            rel1.estado = '0'
            rel2 = Relaciones.objects.get(user_1=usuario, user_2=amigo_usuario, estado='2')
            rel2.estado = '0'
            rel1.save()
            rel2.save()

        else:
            print("wtf2")

    elif 'rechazar_sol' in request.POST:
        amigo_form = UserForm(request.POST)
        if amigo_form.is_valid():
            amigo = amigo_form.cleaned_data['email']
            amigo_usuario = Usuario.objects.get(user__email=amigo)
            usuario = Usuario.objects.get(user=request.user)
            rel1 = Relaciones.objects.get(user_1=amigo_usuario, user_2=usuario, estado='1')
            rel2 = Relaciones.objects.get(user_1=usuario, user_2=amigo_usuario, estado='2')
            rel1.delete()
            rel2.delete()

        else:
            print("wtf3")

    elif 'eliminar_amigo' in request.POST:
        amigo_form = UserForm(request.POST)
        if amigo_form.is_valid():
            amigo = amigo_form.cleaned_data['email']
            amigo_usuario = Usuario.objects.get(user__email=amigo)
            usuario = Usuario.objects.get(user=request.user)
            rel1 = Relaciones.objects.get(user_1=amigo_usuario, user_2=usuario, estado='0')
            rel2 = Relaciones.objects.get(user_1=usuario, user_2=amigo_usuario, estado='0')
            rel1.delete()
            rel2.delete()

        else:
            print("wtf4")

    try:
        solicitudes = Relaciones.objects.filter(user_1__user=request.user, estado='2')

    except Relaciones.DoesNotExist:
        solicitudes = None

    try:
        amigos = Relaciones.objects.filter(user_1__user=request.user, estado='0')

    except Relaciones.DoesNotExist:
        amigos = None

    return render(request, 'UserProfile.html', {'object_list': busqueda, 'sol': solicitudes, 'amigos': amigos})


def login(request):
    if request.method == 'POST':
        login_form = IniciarSesionForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            password = login_form.cleaned_data['password']
            user = authenticate(username=user, password=password)
            if user is not None:
                do_login(request, user)
                return render(request, 'LandingPage.html')
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            name = register_form.cleaned_data['name']
            lastname = register_form.cleaned_data['lastname']
            email = register_form.cleaned_data['email']
            password = register_form.cleaned_data['password']
            try:
                user = User.objects.create_user(username=email, email=email, first_name=name, last_name=lastname,
                                                password=password)
            except:
                return render(request, 'LogIn.html')

            usuario = Usuario(user=user, foto="static/img/turing.jpg")
            usuario.save()
            if user is not None:
                do_login(request, user)
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
            messages.error(request, _('Por favor corrregir el siguiente error.'))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'cambioDeContraseña.html', {
        'form': form
    })


def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            name = register_form.cleaned_data['name']
            lastname = register_form.cleaned_data['lastname']
            email = register_form.cleaned_data['email']
            password = register_form.cleaned_data['password']
            try:
                user = User.objects.create_user(username=email, email=email, first_name=name, last_name=lastname,
                                                password=password)
            except:
                return render(request, 'Register.html')

            usuario = Usuario(user=user, foto="static/img/turing.jpg")
            usuario.save()
            if user is not None:
                do_login(request, user)
                return render(request, 'LandingPage.html')

    return render(request, 'Register.html')


def landing_page_no_loggeados(request):
    return render(request, 'LandingPageNoLoggeados.html')


def LogInStylized(request):
    if request.method == 'POST':
        login_form = IniciarSesionForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            password = login_form.cleaned_data['password']
            user = authenticate(username=user, password=password)
            if user is not None:
                do_login(request, user)
                return render(request, 'LandingPage.html')
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            name = register_form.cleaned_data['name']
            lastname = register_form.cleaned_data['lastname']
            email = register_form.cleaned_data['email']
            password = register_form.cleaned_data['password']
            try:
                user = User.objects.create_user(username=email, email=email, first_name=name, last_name=lastname,
                                                password=password)
            except:
                return render(request, 'LogInStylized.html')

            usuario = Usuario(user=user, foto="static/img/turing.jpg")
            usuario.save()
            if user is not None:
                do_login(request, user)
                return render(request, 'SuccesReg.html')
    return render(request, 'LogInStylized.html')

