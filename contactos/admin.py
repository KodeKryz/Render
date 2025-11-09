from django.contrib import admin
from .models import Contacto
from django.http import HttpResponse
import csv

@admin.action(description='Exportar contactos seleccionados a CSV')
def exportar_contactos_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="contactos.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nombre', 'Teléfono', 'Correo', 'Fecha creación', 'Fecha actualización'])

    for contacto in queryset:
        writer.writerow([
            contacto.nombre,
            contacto.telefono,
            contacto.correo,
            contacto.fecha_creacion.strftime('%Y-%m-%d %H:%M'),
            contacto.fecha_actualizacion.strftime('%Y-%m-%d %H:%M')
        ])
    return response

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'correo', 'fecha_creacion', 'fecha_actualizacion')
    search_fields = ('nombre', 'correo', 'telefono')
    list_filter = ('fecha_creacion',)
    ordering = ('nombre',)
    actions = [exportar_contactos_csv]