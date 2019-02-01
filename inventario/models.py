from django.db import models

# Create your models here

class Inventario(models.Model):

    active = 'actv'
    deactive = 'dctv'

    opciones = (
        (active, 'Activo'),
        (deactive, 'Inactivo',)
    )

    descripcion = models.CharField(max_length = 200)
    marca = models.CharField(max_length = 200)
    caracteristicas = models.TextField(max_length = 500)
    observacion = models.TextField(max_length = 300)
    serial = models.CharField(max_length= 100)
    fecha_ingreso = models.DateTimeField('Fecha de Ingreso')
    estado = models.CharField(max_length=4,choices=opciones, default= active,)

    def __str__(self):
        return '%s %s' % (self.descripcion, self.marca)
