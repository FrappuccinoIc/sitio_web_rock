from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('registrar/', views.registrar, name = "registrar"),
    path('faq/', views.faq, name = "faq"),
    path('redes_sociales/', views.redes_sociales, name = "redes"),
    path('galeria/', views.galeria, name = "galeria"),
]