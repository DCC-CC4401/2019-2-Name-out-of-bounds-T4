from django.shortcuts import render
from .forms import IniciarSesionForm
from .models import Usuario
from .forms import ImageForm

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
        return render(request, 'LogIn.html', {})

def imagenPerfil(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            print("No logro hacer un form valido :c")
            imagen = request.FILES['imagefile']
            newImage = Usuario(foto=imagen)
            newImage.save()

            ultimaimagen = Usuario.objects.last()
            ultimaimagenfile = ultimaimagen.foto

            return render(request, 'UserProfile.html', {'imagefile': ultimaimagenfile})

    else:
        form = ImageForm()
        print("jajaj ayuda2")


    return render(request, 'FormularioCambioImagen.html', {})

