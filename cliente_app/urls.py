from django.urls import path
from cliente_app import views 

urlpatterns = [
    path("clientes",views.inicio_vistaclientes,name="clientes"),
    path("registrarcliente/",views.registrarcliente,name="registrarcliente"),
    path("seleccionarcliente/<id_cliente>",views.seleccionarcliente,name="seleccionarcliente"),
    path("editarcliente/",views.editarcliente,name="editarcliente"),
    path("borrarcliente/<id_cliente>",views.borrarcliente,name="borrarcliente"),
]