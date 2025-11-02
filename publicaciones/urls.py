from django.urls import path
from . import views

urlpatterns = [
    path('', views.foro, name='foro'),
    path('perfil/<int:usuario_id>', views.perfil, name='perfil'),
]