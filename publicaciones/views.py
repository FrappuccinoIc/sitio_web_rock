from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from .models import Publicacion, Categoria
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

@permission_required('publicaciones.delete_publicacion', login_url='/restringido')
def eliminar_post(req, publicacion_id):
    publicacion = Publicacion.objects.get(id = publicacion_id)
    if req.method == "POST":
        publicacion.delete()
        return redirect(reverse('foro'))
    return render(req, "publicaciones/eliminar_post.html", {"publicacion": publicacion})