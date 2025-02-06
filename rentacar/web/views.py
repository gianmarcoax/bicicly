from django.shortcuts import render
from .models import Vehiculo, Nosotros, Contacto, Carrusel, WhatsAppLink

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