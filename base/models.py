from django.db import models

# Create your models here.

class reservamicondominio(models.Model):
    NumeroEdificio = models.IntegerField(primary_key=True)
    NombreResidente = models.CharField(max_length=50)
    Area = models.DecimalField(max_digits=10, decimal_places=2)