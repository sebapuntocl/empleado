from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin): #ordena los campos a mostras en el panel de admin 
    list_display =(
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name', #este campo no existe ene l modelo de bd pero sirve para concatener campos de la tabla ej: nombre y apellido
    )

    #
    def full_name(self, obj): #crea el contenido para mostrar en full_name
        #toda la operacion
        print(obj.first_name)
        return obj.first_name + ' ' + obj.last_name

    search_fields =('first_name',)#teminamos con una coma  // agrega un buscador 
    list_filter = ('departamento','job','habilidades',) #agrega un filtro por trajo y habilidades
    #
    filter_horizontal = ('habilidades',) #agrega un buscador a las habilidades //habilidaes viene del modelo persona


admin.site.register(Empleado,EmpleadoAdmin )