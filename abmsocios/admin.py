from django.contrib import admin
from . import models


@admin.register(models.Socio)
class SocioAdmin(admin.ModelAdmin):
    list_display = ('documento', 'nombre', 'apellido', 'numero_socio',
                    'fecha_inscripcion', 'habilitacion')
    ordering = ('apellido', 'nombre', 'documento', )
    search_fields = ('documento', 'nombre', 'apellido')
    list_filter = ('estado', )


@admin.register(models.Telefono)
class TelefonoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'tipo')
    raw_id_fields = ('socio',)


@admin.register(models.Datos_Medicos)
class DatosMedicosAdmin(admin.ModelAdmin):
    list_display = ('socio', 'obra_social', 'numero_urgencia',
                    'contacto_urgencia', 'contacto_parentesco')
    raw_id_fields = ('socio', )
    ordering = ('socio', )


@admin.register(models.Domicilio)
class DomicilioAdmin(admin.ModelAdmin):
    list_display = ('calle', 'numero', 'piso', 'departamento',
                    'localidad', 'provincia', 'codigo_postal')
    raw_id_fields = ('socio',)


@admin.register(models.ObraSocial)
class ObraSocialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'numero_urgencia')
