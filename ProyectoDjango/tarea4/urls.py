from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', landingpage, name='landingpage'),
    path('imagenPerfil/', imagenPerfil),
    path('login/', login, name='login'),
    path('perfil/',perfil,name='perfil'),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)