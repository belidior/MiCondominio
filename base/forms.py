from django import forms
from .models import reservamicondominio
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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


class ReservaRechazadaForm(forms.Form):
    NumeroEdificio = forms.IntegerField(label='Número de Edificio')
    NombreResidente = forms.CharField(max_length=50, label='Nombre del Residente')
    Area = forms.CharField(max_length=10, label='Área')
    FechaEstimada = forms.DateTimeField(initial=timezone.now, label='Fecha Estimada')

class ReservaAceptadaForm(forms.Form):
    NumeroEdificio = forms.IntegerField(label='Número de Edificio')
    NombreResidente = forms.CharField(max_length=50, label='Nombre del Residente')
    Area = forms.CharField(max_length=10, label='Área')
    FechaEstimada = forms.DateTimeField(initial=timezone.now, label='Fecha Estimada')

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    numeroEdificio = forms.IntegerField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'numeroEdificio')
