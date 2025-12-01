from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User, Group
from publicaciones.models import Usuario
from .forms import UserForm
from django.core.files import File

def home(req):
    return render(req, "core/index.html")

def redes_sociales(req):
    return render(req, "core/redes_sociales.html")

def faq(req):
    return render(req, "core/faq.html")

def galeria(req):
    return render(req, "core/galeria.html")

def registrar(req):
    if req.method == 'POST':
        form = UserForm(req.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if User.objects.filter(username = username).exists():
                return redirect(reverse('registrar') + '?fail')

            user = User.objects.create_user(username = username, password = password)
            usuario = Usuario.objects.create(username = username, account = user)

            # Activar vista staff
            user.is_staff = True
            user.save()
            usuario.save()
            
            group = Group.objects.get(name='Usuarios')  # or Admin
            user.groups.add(group)

            return redirect('home')

    else:
        form = UserForm()

    return render(req, 'core/registrar.html', {'form': form})