from django.contrib import admin

from .models import Asistencia
# Register your models here.

class AsistenciaDisplay(admin.ModelAdmin):
    list_display = ('profesor','materia','seccion','laboratorio_asignado','asistio')

admin.site.register(Asistencia, AsistenciaDisplay)
