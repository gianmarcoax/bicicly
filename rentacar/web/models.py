from django.db import models

class Carrusel(models.Model):
    titulo = models.CharField(max_length=100, blank=True, null=True)  # Campo opcional
    descripcion = models.TextField(blank=True, null=True)  # Campo opcional
    imagen = models.ImageField(upload_to='carrusel/')  # Las imágenes se guardan en media/carrusel/

    def __str__(self):
        return self.titulo if self.titulo else ""

class Vehiculo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='vehiculos/')  # Las imágenes se guardan en media/vehiculos/

    def __str__(self):
        return self.nombre

class Nosotros(models.Model):
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='nosotros/', default='default.jpg')  # Valor predeterminado

    def __str__(self):
        return "Descripción de Nosotros"

class Contacto(models.Model):
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return "Información de Contacto"

class WhatsAppLink(models.Model):
    link = models.URLField(max_length=200, help_text="Enlace de WhatsApp completo (incluyendo https://)")

    def __str__(self):
        return "Enlace de WhatsApp"

    class Meta:
        verbose_name = "Enlace de WhatsApp"
        verbose_name_plural = "Enlace de WhatsApp"