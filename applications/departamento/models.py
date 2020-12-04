from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre',max_length=50)
    short_name = models.CharField('Nombre Corto',max_length=50, unique=True)
    anulate = models.BooleanField('Anulado', default = False)

    class Meta:
        verbose_name = 'Mi Departamento' #Cambia el nombre de la tabla en el admi
        verbose_name_plural = 'Areas de la Empresa' #Cuando es plural cambia el nombre
        ordering =['name'] #ordena de la A-Z
        #ordering =['-name'] #ordena de la Z-A
        #unique_together = ('name','short_name') #indica que valide que no se registre la convinacion similar 
        


    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.short_name
