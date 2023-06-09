# Generated by Django 4.2 on 2023-05-04 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_reservation_delete_solicitud'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('nombre_cliente', models.CharField(max_length=100)),
                ('habitacion', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
    ]
