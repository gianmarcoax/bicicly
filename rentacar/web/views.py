from django.shortcuts import render
from .models import Vehiculo, Nosotros, Contacto, Carrusel

def index(request):
    vehiculos = Vehiculo.objects.all()
    nosotros = Nosotros.objects.first()
    contacto = Contacto.objects.first()
    carrusel = Carrusel.objects.all()
    return render(request, 'index.html', {
        'vehiculos': vehiculos,
        'nosotros': nosotros,
        'contacto': contacto,
        'carrusel': carrusel,
    })