
from django import forms


class CrearMensajeFormulario(forms.Form):
        
    mensaje = forms.CharField(max_length=200, required=False, widget=forms.Textarea)
    