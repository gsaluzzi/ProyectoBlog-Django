from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from home.models import Criticas
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    
    
    return render(request, 'home/home.html', {})


def about(request):
    
    
    return render(request, 'home/about.html', {})



class ListadoCriticas(ListView):
    model = Criticas
    context_object_name = 'listado_de_criticas'
    template_name = 'home/criticas.html'
    
    def get_queryset(self):
        titulo = self.request.GET.get('titulo', '')
        if titulo:
            listado_de_automoviles = self.model.objects.filter(titulo__icontains=titulo)
        else:
            listado_de_automoviles = self.model.objects.all()
        return listado_de_automoviles
    
    
    


class CrearCritica(LoginRequiredMixin, CreateView):
    model = Criticas
    template_name = "home/crear_criticas.html"
    fields = ['titulo', 'critica', 'autor', 'imagen_pelicula', 'fecha_creacion']
    success_url = reverse_lazy('criticas')


class ActualizarCritica(LoginRequiredMixin, UpdateView):
    model = Criticas
    template_name = "home/actualizar_criticas.html"
    fields = ['titulo', 'critica', 'autor', 'imagen_pelicula','fecha_creacion']
    success_url = reverse_lazy('criticas')


class DetalleCritica(DetailView):
    model = Criticas
    template_name = "home/detalle_critica.html"


class EliminarCritica(LoginRequiredMixin, DeleteView):
    model = Criticas
    template_name = "home/eliminar_critica.html"
    success_url = reverse_lazy('criticas')



# Create your views here.
