from django.db import models

#from asistencia.models import Asistencia

# Create your models here.

class Laboratorio(models.Model):
#    profesor_lab = models.ForeignKey(Asistencia, on_delete=models.CASCADE)
    laboratorio = models.CharField(max_length=100)
    maquina = models.IntegerField(default=0)

    def __str__(self):
        return self.laboratorio

