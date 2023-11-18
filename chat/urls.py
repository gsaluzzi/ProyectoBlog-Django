from django.urls import path
from chat.views import ListadoUsuarios, crear_mensaje

urlpatterns = [
    path('usuarios/', ListadoUsuarios.as_view(), name='usuarios_chat'),
    path('sala/<int:user_id>/', crear_mensaje, name='sala_chat'),
  
]


