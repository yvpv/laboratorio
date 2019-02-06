from django.contrib import admin

from .models import Inventario
# Register your models here.

class InventarioAdmin(admin.ModelAdmin):
    fields = [
        'descripcion',
        'marca',
        'serial',
        'caracteristicas',
        'observacion',
        'fecha_ingreso',
        'estado'
    ]

admin.site.register(Inventario, InventarioAdmin)
