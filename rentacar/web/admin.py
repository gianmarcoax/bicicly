from django.contrib import admin
from .models import Vehiculo, Nosotros, Contacto, Carrusel, WhatsAppLink

admin.site.register(Vehiculo)
admin.site.register(Nosotros)
admin.site.register(Contacto)
admin.site.register(Carrusel)

@admin.register(WhatsAppLink)
class WhatsAppLinkAdmin(admin.ModelAdmin):
    list_display = ('link',)