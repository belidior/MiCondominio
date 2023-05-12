from django.db import models
from django.utils import timezone

# Create your models here.

class reservamicondominio(models.Model):
    NumeroEdificio = models.IntegerField(primary_key=True)
    NombreResidente = models.CharField(max_length=50)
    Area = models.CharField(max_length=10)
    FechaEstimada = models.DateTimeField(default=timezone.now)

    objects = models.Manager()

    def __str__(self):
        return self.NumeroEdificio



class reservarechazada(models.Model):
    NumeroEdificio = models.IntegerField(primary_key=True)
    NombreResidente = models.CharField(max_length=50)
    Area = models.CharField(max_length=10)
    FechaEstimada = models.DateTimeField(default=timezone.now)

    objects = models.Manager()

    def __str__(self):
        return self.NumeroEdificio
    

class reservaaceptada(models.Model):
    NumeroEdificio = models.IntegerField(primary_key=True)
    NombreResidente = models.CharField(max_length=50)
    Area = models.CharField(max_length=10)
    FechaEstimada = models.DateTimeField(default=timezone.now)

    objects = models.Manager()

    def __str__(self):
        return self.NumeroEdificio