from django.shortcuts import render

# Create your views here.
def landingpage(request):
    return render(request, 'LandingPage.html')

def perfil(request):
    return render(request, 'UserProfile.html')