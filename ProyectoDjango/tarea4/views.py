from django.shortcuts import render
from .forms import IniciarSesionForm

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
