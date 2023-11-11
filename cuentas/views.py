from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from cuentas.forms import MiFormularioDeCreacion, EdicionPerfil

def login(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contra = formulario.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)
            
            django_login(request, user)
            
            # DatosExtra.objects.get_or_create(user=request.user)
            
            return redirect('home')
              
    return render(request, 'cuentas/login.html', {'formulario_de_login': formulario})


def registro(request):
    formulario = MiFormularioDeCreacion()
    
    if request.method == 'POST':
        formulario = MiFormularioDeCreacion(request.POST)
        if formulario.is_valid():
            
            formulario.save()
            
            return redirect('login')
            
    return render(request, 'cuentas/registro.html', {'formulario_de_registro': formulario})



def editar_perfil(request):
    
      
    formulario = EdicionPerfil(instance=request.user)
    
    if request.method == 'POST':
        formulario = EdicionPerfil(request.POST, instance=request.user)
        
        if formulario.is_valid():         

          
            formulario.save()            
            
    
    return render(request, 'cuentas/editar_perfil.html', {'formulario': formulario})

class CambiarPassword(PasswordChangeView):
    template_name = 'cuentas/cambiar_password.html'
    success_url = reverse_lazy('editar_perfil')

# Create your views here.
