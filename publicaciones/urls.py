from django.urls import path
from . import views

urlpatterns = [
    path('', views.foro, name='foro'),
    path('perfil/<int:usuario_id>', views.perfil, name='perfil'),
    path('perfil/eliminar/<int:usuario_id>', views.eliminar_usuario, name='eliminar_usuario'),
    path('restringido', views.restringido, name='restringido'),
]