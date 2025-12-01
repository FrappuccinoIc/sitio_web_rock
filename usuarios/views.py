from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group
from .models import Usuario
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
            usuario = Usuario.objects.create(username = username, cuenta = user)

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
            usuario = Usuario.objects.create(username = username, cuenta = user)

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

@login_required
def perfil(req, usuario_id):
    #usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario = Usuario.objects.get(id = usuario_id)
    return render(req, "usuarios/perfil.html", {"usuario": usuario})

@permission_required('usuarios.delete_usuario', login_url='/restringido')
def eliminar_usuario(req, usuario_id):
    usuario = Usuario.objects.get(id = usuario_id)
    cuenta = User.objects.get(id = usuario.cuenta.id)
    if req.method == "POST":
        usuario.delete()
        cuenta.delete()
        return redirect(reverse('foro'))
    return render(req, "usuarios/eliminar_usuario.html", {"usuario": usuario})