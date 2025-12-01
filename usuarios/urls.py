from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar, name = "registrar"),
    path('registrar/admin', views.registrar_admin, name = "registrar_admin"),
    path('perfil/<int:usuario_id>', views.perfil, name='perfil'),
    path('perfil/eliminar/<int:usuario_id>', views.eliminar_usuario, name='eliminar_usuario'),
]