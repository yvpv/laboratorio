from django.db import models

from laboratorio.models import Laboratorio

# Create your models here.
class Asistencia(models.Model):
    profesor = models.CharField(max_length= 200)
    materia = models.CharField(max_length= 200)
    seccion = models.IntegerField(default=0)
    laboratorio_asignado = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    entrada = models.TimeField('Hora Entrada')
    salida = models.TimeField('Hora Salida')
    asistio = models.BooleanField(default = True)

    def __str__(self):
        return '%s %s' % (self.profesor, self.materia)
