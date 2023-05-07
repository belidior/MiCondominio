from django.db import models

# Create your models here.

class reservamicondominio(models.Model):
    NumeroEdificio = models.IntegerField(primary_key=True)
    NombreResidente = models.CharField(max_length=50)
    Area = models.CharField(max_length=10)


    