from django.db import models

# Create your models here.

class Inventario(models.Model):
    descripcion = models.CharField(max_length = 200)
    marca = models.CharField(max_length = 200)
    caracteristicas = models.TextField(max_length = 500)
    estado = models.CharField(max_length = 200)

    def __str__(self):
        return '%s %s' % (self.descripcion, self.marca)
