from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    username = models.CharField(max_length=40, verbose_name="Nombre de Usuario")
    descripcion = models.TextField(verbose_name = "Descripción", default="Sin descripción")
    imagen = models.ImageField(upload_to="projects", verbose_name="Perfil", default="projects\default.jpg", blank=True, null=True)
    #cuenta = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Cuenta enlazada")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última vez actualizado")

    def __str__(self): return self.username