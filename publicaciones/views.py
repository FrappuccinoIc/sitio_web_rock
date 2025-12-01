from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from .models import Publicacion, Usuario, Categoria
from django.contrib.auth.models import User
from django.core.paginator import Paginator

def foro(req):
    # Base: todas las publicaciones
    publicaciones = Publicacion.objects.all()

    # Filtros
    q = req.GET.get('q')
    categoria = req.GET.get('categoria')

    if q:
        publicaciones = publicaciones.filter(titulo__icontains=q)

    if categoria:
        publicaciones = publicaciones.filter(categorias__id=categoria)

    # Paginación
    p = Paginator(publicaciones, 4)
    page_number = req.GET.get('page')
    page_obj = p.get_page(page_number)

    # Rango visual de paginación
    index = page_obj.number - 1
    max_index = len(p.page_range)
    start_index = max(index - 2, 0)
    end_index = min(index + 3, max_index)
    page_range = p.page_range[start_index:end_index]

    # Para mostrar opciones en <select>
    categorias = Categoria.objects.all()

    return render(req, "publicaciones/foro.html", {
        "page_obj": page_obj,
        "page_range": page_range,
        "categorias": categorias,
    })

@login_required
def perfil(req, usuario_id):
    #usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario = Usuario.objects.get(id = usuario_id)
    return render(req, "publicaciones/perfil.html", {"usuario": usuario})

@permission_required('usuarios.delete_usuario', login_url='/foro/restringido')
def eliminar_usuario(req, usuario_id):
    usuario = Usuario.objects.get(id = usuario_id)
    cuenta = User.objects.get(id = usuario.account.id)
    if req.method == "POST":
        usuario.delete()
        cuenta.delete()
        return redirect(reverse('foro'))
    return render(req, "publicaciones/eliminar_usuario.html", {"usuario": usuario})

@permission_required('publicaciones.delete_publicacion', login_url='/foro/restringido')
def eliminar_post(req, publicacion_id):
    publicacion = Publicacion.objects.get(id = publicacion_id)
    return render(req, "publicaciones/eliminar_post.html", {"publicacion": publicacion})

def restringido(req):
    return render(req, "publicaciones/restringido.html")