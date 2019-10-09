from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    foto = models.ImageField(upload_to='fotitos')

class HistorialDeActividades(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    init_time = models.TimeField()
    date = models.DateField()
    duration = models.TimeField()
    user = models.ForeignKey(Usuario, models.SET_NULL , null=True, blank=True)

    class Meta:
        unique_together = (("init_time","date","user"))

class ActividadesTipo(models.Model):
    user = models.ForeignKey(Usuario, models.SET_NULL, null=True, blank= True)
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

class Admin(models.Model):
    admin_user = models.OneToOneField(User,models.CASCADE)

class Relaciones(models.Model):
    user_1 = models.ForeignKey(Usuario, models.SET_NULL, null=True, blank=True, related_name="Owner")
    user_2 = models.ForeignKey(Usuario, models.SET_NULL, null=True, blank=True, related_name="Other")
    estado = models.CharField(max_length=50);