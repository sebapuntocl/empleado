from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('prueba/', views.PruebaView.as_view(), name=""),
    path('lista/', views.pruebaListView.as_view(), name="lista"),
    path('lista_prueba/', views.ListaPrueba.as_view(), name="listar"),
    path('add/', views.PruebaCreateView.as_view(), name="prueba_add"),
    path('resumen/', views.ResumeFoundationView.as_view(), name="resumen_foundation"),
]
