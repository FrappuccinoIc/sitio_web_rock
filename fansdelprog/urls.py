from django.contrib import admin
from django.urls import path, include
from core import views as views_core
from publicaciones import views as views_publicacion # Importar las funciones o métodos que quieres ejecutar al acceder una ruta
from django.conf import settings

from django.conf.urls.static import static

# Guardar cada nueva ruta aqui
urlpatterns = [
    path('', views_core.home, name = 'home'), # ('ruta de acceso, ej: tupagina.com/foro/comentarios/:id', función o método a ejecutar al acceder, alias de ruta)
    path('faq/', views_core.faq, name='faq'),
    path('redes_sociales/', views_core.redes_sociales, name='redes'),
    path('galeria/', views_core.galeria, name='galeria'),
    path('foro/', views_publicacion.foro, name='foro'),
    path('perfil/<int:usuario_id>', views_publicacion.perfil, name='perfil'),
    path('contacto/', include("contacto.urls")),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)