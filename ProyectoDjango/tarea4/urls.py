from django.urls import path
from .views import *

urlpatterns = [
    path('', landingpage, name='landingpage'),
    path('perfil/',perfil,name='perfil'),
]