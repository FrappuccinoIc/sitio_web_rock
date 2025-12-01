from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User, Group
from publicaciones.models import Usuario
from .forms import UserForm

def registrar(req):
    if req.method == 'POST':
        form = UserForm(req.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password != confirm_password:
                return redirect(reverse('registrar') + '?pass')

            if User.objects.filter(username = username).exists():
                return redirect(reverse('registrar') + '?fail')

            user = User.objects.create_user(username = username, password = password)
            usuario = Usuario.objects.create(username = username, account = user)

            # Activar vista staff
            user.is_staff = True
            user.save()
            usuario.save()
            
            group = Group.objects.get(name='Usuarios')
            user.groups.add(group)

            return redirect('home')

    else:
        form = UserForm()

    return render(req, 'usuarios/registrar.html', { 'form': form })

def registrar_admin(req):
    if req.method == 'POST':
        form = UserForm(req.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password != confirm_password:
                return redirect(reverse('registrar_admin') + '?pass')

            if User.objects.filter(username = username).exists():
                return redirect(reverse('registrar_admin') + '?fail')

            user = User.objects.create_user(username = username, password = password)
            usuario = Usuario.objects.create(username = username, account = user)

            # Activar vista staff
            user.is_staff = True
            user.save()
            usuario.save()
            
            group = Group.objects.get(name='Administradores')
            user.groups.add(group)

            return redirect('home')

    else:
        form = UserForm()

    return render(req, 'usuarios/registrar_admin.html', { 'form': form })