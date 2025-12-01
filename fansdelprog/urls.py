from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from django.conf.urls.static import static

# Guardar cada nueva ruta aqui
urlpatterns = [
    path('', include("core.urls")),
    path('contacto/', include("contacto.urls")),
    path('foro/', include("publicaciones.urls")),
    path('usuarios/', include("usuarios.urls")),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)