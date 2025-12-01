from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Publicacion, Usuario
from django.core.paginator import Paginator

def foro(req):
    publicacion=Publicacion.objects.all()
    p = Paginator(publicacion, 4)

    page_number = req.GET.get('page') # Se pasa la url que se quiere conseguir, en este caso: ?page=n
    page_obj = p.get_page(page_number)

    # Rango de páginas visibles (ejemplo: 5)
    index = page_obj.number - 1  # Índice actual. Paginator.number nos da un número indexeado a 1, no a 0. Se resta para mantener una indexación de 0 para el rango
    max_index = len(p.page_range) # Consigue la cantidad de paginas en relación con la cantidad de objetos por página
    start_index = max(index - 2, 0)
    end_index = min(index + 3, max_index)
    page_range = p.page_range[start_index:end_index]

    return render(req, "publicaciones/foro.html", {
        "page_obj": page_obj,
        "page_range": page_range,  # se pasa al template
    })

@login_required
def perfil(req, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario = Usuario.objects.get(id = usuario_id)
    # Añadir página 404 con manejo de errores
    return render(req, "publicaciones/perfil.html", {"usuario": usuario})