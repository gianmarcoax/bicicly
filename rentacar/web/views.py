from django.shortcuts import render
from .models import Vehiculo, Nosotros, Contacto, Carrusel, WhatsAppLink
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    vehiculos = Vehiculo.objects.all()
    nosotros = Nosotros.objects.first()
    contacto = Contacto.objects.first()
    carrusel = Carrusel.objects.all()
    whatsapp_link = WhatsAppLink.objects.first()  # Obtener el enlace de WhatsApp

    return render(request, 'index.html', {
        'vehiculos': vehiculos,
        'nosotros': nosotros,
        'contacto': contacto,
        'carrusel': carrusel,
        'whatsapp_link': whatsapp_link,  # Pasar el enlace a la plantilla
    })

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')

        # Enviar correo electrónico
        send_mail(
            f'Mensaje de {nombre}',  # Asunto
            f"De: {email}\n\n{mensaje}",  # Cuerpo del mensaje
            settings.DEFAULT_FROM_EMAIL,  # Remitente
            [settings.EMAIL_HOST_USER],  # Destinatario
            fail_silently=False,
        )

        # Mostrar mensaje de éxito
        messages.success(request, '¡Tu mensaje ha sido enviado correctamente!')
        return redirect('index')  # Redirigir a la página de inicio

    return redirect('index')  # Si no es POST, redirigir a la página de inicio