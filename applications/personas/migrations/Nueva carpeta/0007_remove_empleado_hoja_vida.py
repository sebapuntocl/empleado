# Generated by Django 2.2.6 on 2020-12-04 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0006_empleado_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='hoja_vida',
        ),
    ]