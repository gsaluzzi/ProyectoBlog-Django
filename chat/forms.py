
from django import forms


class CrearMensajeFormulario(forms.Form):
        
    mensaje = forms.CharField(max_length=100)
    