from django.contrib import admin
from .models import Publicacion, Categoria
    
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('titulo', 'usuario', 'created')
    ordering=('created', 'titulo', 'usuario')
    list_filter=('categorias', 'created')
    search_fields=('titulo', 'usuario__username')

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Publicacion,ProjectAdmin)