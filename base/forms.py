from django import forms
from .models import reservamicondominio

class reservamicondominio(forms.ModelForm):
    class Meta:
        model = reservamicondominio
        fields = ['NumeroEdificio', 'NombreResidente','Area']
