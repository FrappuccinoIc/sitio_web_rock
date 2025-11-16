from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    username = models.CharField(max_length=40, verbose_name="Nombre de Usuario")
    descripcion = models.TextField(verbose_name = "Descripción")
    imagen = models.ImageField(upload_to="projects", verbose_name="Perfil")
    account = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Cuenta relacionada")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última vez actualizado")

    def __str__(self): return self.username

class Categoria(models.Model):
    nombre = models.CharField(max_length = 50, verbose_name = "Nombre")
    descripcion = models.CharField(max_length = 100, verbose_name = "Descripción", default='')
    
    created = models.DateTimeField(auto_now = True, verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha de edición")

    def __str__(self): return self.nombre

class Publicacion(models.Model):
    titulo = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    descripcion = models.TextField(verbose_name = "Descripción")
    imagen = models.ImageField(upload_to="projects", verbose_name="Imagen")
    categorias = models.ManyToManyField(Categoria, verbose_name = "Categorias")

    class Meta:
        verbose_name = "publicación"
        verbose_name_plural = "publicaciones"

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self): return self.titulo