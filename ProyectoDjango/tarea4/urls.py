from django.urls import path
from .views import *

urlpatterns = [
    path('', register, name='register'),
    path('', login, name='login'),
    path('', landingpage, name='landingpage'),
    path('perfil/',perfil,name='perfil'),
]