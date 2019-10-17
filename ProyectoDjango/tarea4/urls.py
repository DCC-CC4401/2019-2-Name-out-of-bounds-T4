from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('inicio/', landingpage, name='landingpage'),
    path('perfil/',perfil,name='perfil'),
    path('logout/',logout,name='logout')
]