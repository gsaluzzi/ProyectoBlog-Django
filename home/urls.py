from home.views import home, about
from django.urls import path
from home.views import ListadoCriticas, CrearCritica

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about" ),
    path('criticas/', ListadoCriticas.as_view(), name='criticas'),
    path('criticas/crear/', CrearCritica.as_view(), name='crear_critica'),
   
]