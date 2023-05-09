from django import forms
from .models import reservamicondominio

class reservamicondominio(forms.ModelForm):
    AREA_CHOICES = (
        ('Piscina', 'Piscina'),
        ('Salon de eventos', 'Salon de eventos'),
        ('Gimnasio', 'Gimnasio'),
        ('Quincho', 'Quincho'),
    )

    Area = forms.ChoiceField(choices=AREA_CHOICES)

    class Meta:
        model = reservamicondominio
        fields = ['NumeroEdificio', 'NombreResidente', 'Area', 'FechaEstimada']
