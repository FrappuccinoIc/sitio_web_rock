from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from .forms import ContactForm

def contacto(req):
    form = ContactForm()

    if req.method == "POST":
        form = ContactForm(req.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            content = form.cleaned_data.get('content')

            mensaje = f"Mensaje de {name} <{email}>:\n\n{content}"

            send_mail(
                subject="Nuevo mensaje desde el formulario de contacto",
                message=mensaje,
                from_email=email,
                recipient_list=["sandbox.smtp.mailtrap.io"],  # Mailtrap te da uno propio
            )

            return redirect(reverse('contacto') + '?ok')

    return render(req, 'contacto/contacto.html', {"form": form})
