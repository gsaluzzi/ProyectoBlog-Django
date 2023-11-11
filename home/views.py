from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from home.models import Criticas

def home(request):
    
    
    return render(request, 'home/home.html', {})


def about(request):
    
    
    return render(request, 'home/about.html', {})



class ListadoCriticas(ListView):
    model = Criticas
    context_object_name = 'listado_de_criticas'
    template_name = 'home/criticas.html'


class CrearCritica(CreateView):
    model = Criticas
    template_name = "home/crear_criticas.html"
    fields = ['titulo', 'critica', 'autor', 'fecha_creacion']
    success_url = reverse_lazy('criticas')



# Create your views here.
