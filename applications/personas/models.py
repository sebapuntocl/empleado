from django.db import models
from applications.departamento.models import Departamento #llamamos a la tabla departamnto

#from .fields import RichTextField # importa CKEditor

# Create your models here.
class Habilidades(models.Model):
    habilidades = models.CharField("Habilidades", max_length=50)

    class Meta:
        verbose_name = 'Hbilidad' #Cambia el nombre de la tabla en el admi
        verbose_name_plural = 'Habiolidades Empliados' #Cuando es plural cambia el nombre

    def __str__(self):
        return self.habilidades

class Empleado(models.Model):
    JOB_CHOICES =(
        ('0',"Contador"),
        ('1',"Administrador"),
        ('2',"Economista"),
        ('3',"Otro"),
    )
    # Modelo para tabla empleado
    #contador
    #administrador
    #economista
    #otro

    first_name = models.CharField("Nombres", max_length=50)
    last_name = models.CharField("Apellidos", max_length=50)
    full_name = models.CharField("Nombre Completo", max_length=120, blank=True)
    job = models.CharField ("Trabajo", max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE) #crea la relacion con tabla departamento
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades) #crea la relacion muchos a muchos con la taba habilidades
    # hoja_vida = RichTextField() # este campo se va a crear con ckeditor. despues hacer denuevo la migracion
    
    class Meta:
        verbose_name = 'Empleado' #Cambia el nombre de la tabla en el admi
        verbose_name_plural = 'Mis Empleados' #Cuando es plural cambia el nombre
        ordering =['first_name'] #ordena de la A-Z
       


    def __str__(self):
        return self.first_name + ' - ' + self.last_name