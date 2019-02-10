from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Laboratorio(models.Model):
    laboratorio = models.CharField(max_length=100)
    maquina = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(100)])

    def __str__(self):
        return self.laboratorio

