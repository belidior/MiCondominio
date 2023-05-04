# Generated by Django 4.2 on 2023-05-04 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_rename_habitacion_reserva_area'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservaAreasComunes',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('NombreResidente', models.CharField(max_length=100)),
                ('NumeroEdificio', models.IntegerField()),
                ('Area', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Reserva',
        ),
    ]