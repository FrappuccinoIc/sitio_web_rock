from django.shortcuts import render
from django.contrib.auth import logout

def home(req):
    cerrar_sesion = req.GET.get('salir')
    if cerrar_sesion == "si" and req.user.is_authenticated:
        logout(req)
    return render(req, "core/index.html")

def redes_sociales(req):
    return render(req, "core/redes_sociales.html")

def faq(req):
    return render(req, "core/faq.html")

def galeria(req):
    return render(req, "core/galeria.html")

def restringido(req):
    return render(req, "core/restringido.html")