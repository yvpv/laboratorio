from django.db import models

# Create your models here.

class Laboratorio(models.Model):
    laboratorio = models.CharField(max_length=100)
    maquina = models.IntegerField(default=0)

    def __str__(self):
        return self.laboratorio

