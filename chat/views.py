from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from chat.forms import CrearMensajeFormulario
from chat.models import Mensaje

class ListadoUsuarios(ListView):
    model = User
    context_object_name = 'listado_de_usuarios'
    template_name = 'chat/lista_usuarios.html'


# def crear_sala(request, user_id):
#    usuario = User.objects.get(id=user_id)
#    print(usuario)
        
#    return render(request, 'chat/conversacion.html', {'usuario':usuario})



def crear_mensaje(request, user_id):  
    usuario = User.objects.get(id=user_id)
    listado_de_mensajes = Mensaje.objects.all()
        
    if request.method == 'POST':        
        formulario = CrearMensajeFormulario(request.POST)

        mensaje = request.POST.get('mensaje')
        emisor = request.user.username
        destinatario = usuario.username
        mensaje = Mensaje(mensaje=mensaje, destinatario=destinatario, emisor=emisor)
        mensaje.save()     
    formulario = CrearMensajeFormulario()
    return render(request, 'chat/conversacion.html', {'formulario_mensaje': formulario,'usuario':usuario, 'listado_de_mensajes':listado_de_mensajes})





# Create your views here.
