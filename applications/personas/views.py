from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
    )

#importo modelo empleados de ls bd
from .models import Empleado
#importamos el forms
from .forms import EmpleadoForm

class InivioViews(TemplateView):
    #vista carga la apgina de inicio
    template_name = 'inicio.html'



# 1.- Listar todos los empleados de la empresa
class LitsAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    # paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        # print('++++++++++++++')
        palabra_clave = self.request.GET.get("kwords",'')
        lista = Empleado.objects.filter(
            last_name__icontains=palabra_clave
        )
        return lista


class LitsByAreaEmpleado(ListView):
    """ lista empleados de un area """
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        area = self.kwargs['shortname']
        lista = queryset = Empleado.objects.filter(
        departamento__short_name=area  #el nombre viene del archivo model de la base de datos y el nombre del campo a buscasar poner dos 
        ) #guiones
        return lista

class LitsEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado
      

class LitsByAreaTrabajo(ListView):
    template_name = 'persona/list_by_trabajo.html'
    

    def get_queryset(self):
        trabajo = self.kwargs['shortname']
        lista = queryset = job.objects.filter(
        job = trabajo  #el nombre viene del archivo model de la base de datos y el nombre del campo a buscasar poner dos guiones
        )
        return lista

class ListEmpleadosByKword(ListView):
    
    template_name = 'persona/by_kwords.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('++++++++++++++')
        palabra_clave = self.request.GET.get("kwords",'')
        lista = queryset = Empleado.objects.filter(
        first_name = palabra_clave 
        )
        return lista
    

# 5.- Listar habilidades de un empleado

class ListHabiliadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        
        habilidad = self.request.GET.get("cosas",'')
        lista = queryset = Empleado.objects.filter(
        habilidades = habilidad 
        )
        return lista
    
        # mpleado = Empleado.objects.get(id=3)
        # return empleado.habilidades.all()e
    

# ------------- DetailView------
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        #
        context["titulo"] = 'El empleado del mes'  
        return context

# ------ CreateView----
class SuccessView(TemplateView):
    template_name = "persona/success.html"

# solo las 4 primeras  nesecita estos 4 campos para funcionar   

class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    form_class = EmpleadoForm
   # fields = ('__all__') # este campo muestra todos los campos del formulario
    # fields = [
    #     'first_name',
    #     'last_name',
    #     'job',
    #     'departamento',
    #     'habilidades',
    #     'avatar',
    # ]
    #success_url = '.' # con '.' es para que se recargue en la misma pagina
    success_url = reverse_lazy('persona_app:empleados_admin')

    #valoda el formulario
    def form_valid(self, form):
        #logica del proceso
        empleado = form.save(commit=False) #guarda la instancia en ram pero no la guarda en la bd
        empleado.full_name = empleado.first_name +' '+ empleado.last_name
        empleado.save()

        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    #los mismos fields son los que voy a modificar
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('***********METODO POST**********')
        print('=======================')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)
    
    #valida el formulario
    def form_valid(self, form):
        #logica del proceso
        print('********METODO form valid*********')
        print('****************************')
        return super(EmpleadoUpdateView, self).form_valid(form)




class EmpleadoDeleteView(DeleteView):
    template_name = "persona/delete.html"
    model = Empleado

    success_url = reverse_lazy('persona_app:empleados_admin')



    

