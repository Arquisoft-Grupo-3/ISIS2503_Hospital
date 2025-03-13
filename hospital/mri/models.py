from django.db import models

from usuarios.models import Usuario
# Create your models here.
class MRI(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None)
    fecha = models.DateField()
    hora = models.TimeField()
    descripcion = models.TextField()