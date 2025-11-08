from django.contrib import admin
from .models import Contacto

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'correo', 'fecha_creacion', 'fecha_actualizacion')
    search_fields = ('nombre', 'correo', 'telefono')
    list_filter = ('fecha_creacion',)
    ordering = ('nombre',)