from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar, name = "registrar"),
    path('registrar/admin', views.registrar_admin, name = "registrar_admin"),
]