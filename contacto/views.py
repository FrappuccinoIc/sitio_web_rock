from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from .forms import ContactForm

def contacto(req):
    contact_form = ContactForm()
    if req.method == "POST":
        contact_form = ContactForm(data = req.POST)
        if contact_form.is_valid():
            # get de un POST siempre debe conseguir una tupla al menos. Ya que nosotros queremos solo un valor, el segundo valor estará vacío.
            name = req.POST.get('name', '')
            email = req.POST.get('email', '')
            content = req.POST.get('content', '')
            return redirect(reverse('contacto') + '?ok')

    return render(req, 'contacto/contacto.html', {"form": contact_form})