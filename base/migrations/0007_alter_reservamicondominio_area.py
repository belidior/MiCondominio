# Generated by Django 4.2 on 2023-05-05 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_reservamicondominio_delete_reservaareascomunes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservamicondominio',
            name='Area',
            field=models.CharField(max_length=10),
        ),
    ]
