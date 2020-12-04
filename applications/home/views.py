from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView
    )
#importo la tabla 
from .models import Prueba

from .forms import PruebaForm
# Create your views here.

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'

class ResumeFoundationView(TemplateView):
    template_name = 'home/resume_fundation.html'


class pruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'lista_numeros'
    queryset = ['0','1','10','20','30']


class ListaPrueba(ListView):
    template_name = "home/lista_prueba.html"
    model = Prueba
    context_object_name = 'lista'

class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    form_class = PruebaForm
    success_url = '/'




