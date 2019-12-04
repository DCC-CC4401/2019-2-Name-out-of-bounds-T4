from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from tarea4 import views

urlpatterns = [
    path('', landing_page_no_loggeados),
    path('login/', login, name='login'),
    path('landing_page_no_loggeados/', landing_page_no_loggeados, name='landing_page_no_loggeados'),
    path('register/', register, name='register'),
    path('LogInStylized/', LogInStylized, name='LogInStylized'),
    path('inicio/', landingpage, name='landingpage'),
    path('perfil/', perfil, name='perfil'),
    path('logout/', logout, name='logout'),
    path('perfil/cambioImagen/', cambioImagen, name='cambioImagen'),
    url('perfil/cambioContraseña/', views.cambioContraseña, name='cambioContraseña'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
