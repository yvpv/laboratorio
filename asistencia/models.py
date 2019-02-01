from django.db import models

# Create your models here.
class Asistencia(models.Model):
    profesor = models.CharField(max_length= 200)
    materia = models.CharField(max_length= 200)
    seccion = models.IntegerField
    dia = models.DateTimeField('Fecha asistencia')
    asistio = models.BooleanField

    def __str__(self):
        return '%s %s' % (self.profesor, self.materia)
