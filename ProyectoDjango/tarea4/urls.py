from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', login),
    path('login/', login, name='login'),
    path('inicio/', landingpage, name='landingpage'),
    path('perfil/',perfil,name='perfil'),
    path('logout/',logout,name='logout'),
    path('perfil/cambioImagen/',cambioImagen, name='cambioImagen')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)