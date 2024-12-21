from django.db import models
from django.contrib.auth.models import User

class Tarea(models.Model):
    titulo =models.CharField(max_length=50)
    descripcion =models.TextField(max_length=100)
    fecha_limite = models.DateField(null=True)
    categoria = models.CharField(max_length=20)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    importante = models.BooleanField(default=False)
    public = models.BooleanField(default=False)
    hecho = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

