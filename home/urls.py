from home.views import home, about
from django.urls import path
from home.views import ListadoCriticas, CrearCritica, ActualizarCritica, DetalleCritica, EliminarCritica

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about" ),
    path('criticas/', ListadoCriticas.as_view(), name='criticas'),
    path('criticas/crear/', CrearCritica.as_view(), name='crear_critica'),
    path('criticas/<int:pk>/', DetalleCritica.as_view(), name='detalle_critica'),
    path('criticas/<int:pk>/actualizar/', ActualizarCritica.as_view(), name='actualizar_critica'),
    path('criticas/<int:pk>/eliminar/', EliminarCritica.as_view(), name='eliminar_critica'),
   
]