from django.contrib import admin
from .models import Publicacion, Categoria, Usuario

class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('titulo', 'usuario', 'created')
    ordering=('created', 'titulo', 'usuario')
    list_filter=('categorias', 'created')
    search_fields=('titulo', 'usuario__username')

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Publicacion,ProjectAdmin)