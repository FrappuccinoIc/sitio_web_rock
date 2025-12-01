from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group, Permission
from .models import Usuario
from .forms import UserForm

def conseguir_crear_grupo(grupo, perm_strings):
    group, created = Group.objects.get_or_create(name=grupo) # consigueme un grupo que exista con este nombre. Si no existe, crealo, y dime con un booleano si justo se creo

    for perm_string in perm_strings:
        app_label, codename = perm_string.split('.')
        perm = Permission.objects.get(
            content_type__app_label = app_label,
            codename = codename.split('_', 1)[1]  # remove app prefix if needed
        )
        group.permissions.add(perm)

    return group

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
            
            group_perms = {
                'publicaciones.add_publicacion',
                'usuarios.view_usuario', 'usuarios.change_usuario',
                'publicaciones.view_usuario', 'auth.view_user',
                'auth.delete_user', 'publicaciones.view_categoria',
            }

            group = conseguir_crear_grupo("Usuarios", group_perms)
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
            
            group_perms = {
                'sessions.add_session', 'publicaciones.change_usuario', 'auth.delete_group',
                'publicaciones.change_categoria', 'publicaciones.delete_usuario', 'auth.delete_permission',
                'admin.add_logentry', 'admin.delete_logentry', 'usuarios.add_usuario', 'contenttypes.add_contenttype',
                'publicaciones.add_usuario', 'sessions.view_session', 'auth.delete_user', 'publicaciones.view_usuario',
                'sessions.delete_session', 'admin.view_logentry', 'sessions.change_session', 'auth.change_user',
                'auth.view_user', 'auth.view_group', 'auth.change_permission', 'auth.change_group', 'usuarios.view_usuario',
                'publicaciones.add_publicacion', 'publicaciones.view_categoria', 'publicaciones.view_publicacion',
                'publicaciones.delete_publicacion', 'admin.change_logentry', 'auth.add_group', 'auth.add_user',
                'publicaciones.add_categoria', 'auth.view_permission', 'contenttypes.view_contenttype', 'contenttypes.change_contenttype',
                'contenttypes.delete_contenttype', 'usuarios.delete_usuario', 'auth.add_permission', 'publicaciones.delete_categoria'
            }

            group = conseguir_crear_grupo("Administradores", group_perms)
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