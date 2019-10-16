from django.urls import path
from .views import *

urlpatterns = [
    path('registro/', register, name='register'),
    path('login/', login, name='login'),
    path('inicio/', landingpage, name='landingpage'),
    path('perfil/',perfil,name='perfil'),
    path('login/',logout,name='logout')
]