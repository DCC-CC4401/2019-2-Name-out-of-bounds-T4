from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Usuario: usuario que va a utilizar la app
# La información que se guardará:
# Nombre y Apellido
# Correo (llave de este modelo) (Ver como agregar)
# Password
# Imagen de perfil
class Usuario(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    foto = models.ImageField(upload_to='fotitos')

# Actividades: Historial de todas las actividades que
# realizan los usuarios.
# Información de cada actividad:
# Nombre, Categoría
# Descripción breve de la actividad
# Fecha, hora de inicio y duración
# Usuario quien realiza la actividad
# Llave: usuario, fecha y hora de inicio de la actividad
class Actividad(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    init_time = models.TimeField()
    date = models.DateField()
    duration = models.TimeField()
    user = models.ForeignKey(Usuario, models.SET_NULL , null=True, blank=True)

    class Meta:
        unique_together = (("init_time","date","user"))

# ActividadesTipo: Actividades predefinidas por los usuarios
# Son solo fichas con posibles actividades a realizar, pero no
# representan una actividad hecha.
# Información que contienen las actividades tipo:
# Usuario a quien pertenece esta actividad
# Categoría, nombre y descripción.
# Su llave en este caso será el usuario y el nombre(?)
class ActividadesTipo(models.Model):
    user = models.ForeignKey(Usuario, models.SET_NULL, null=True, blank= True)
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

# Admin: Administrador de la aplicación
# Información de esta tabla:
# Correo y password
class Admin(models.Model):
    admin_user = models.OneToOneField(User,models.CASCADE)

# Relaciones: representa las relaciones entre dos usuarios
# Owner: quien envía/o la solicitud
# Other: quien recibe la solicitud
# estado: 0 {No hay relación}, 1 {Solicitud}, 2 {Amigos}
class Relaciones(models.Model):
    user_1 = models.ForeignKey(Usuario, models.SET_NULL, null=True, blank=True, related_name="Owner")
    user_2 = models.ForeignKey(Usuario, models.SET_NULL, null=True, blank=True, related_name="Other")
    estado = models.IntegerField(default=0)