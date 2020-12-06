# Generated by Django 2.2.6 on 2020-10-29 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidades', models.CharField(max_length=50, verbose_name='Habilidades')),
            ],
            options={
                'verbose_name': 'Hbilidad',
                'verbose_name_plural': 'Habiolidades Empliados',
            },
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['first_name'], 'verbose_name': 'Mi Departamento', 'verbose_name_plural': 'Areas de la Empresa'},
        ),
    ]