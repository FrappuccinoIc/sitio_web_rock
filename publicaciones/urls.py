from django.urls import path
from . import views

urlpatterns = [
    path('', views.foro, name='foro'),
    path('eliminar/<int:publicacion_id>', views.eliminar_post, name='eliminar_post'),
]