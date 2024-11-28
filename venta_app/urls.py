from django.urls import path
from venta_app import views 

urlpatterns = [
    path("ventas",views.inicio_vistaventas,name="ventas"),
    path("registrarventa/",views.registrarventa,name="registrarventa"),
    path("seleccionarventa/<id_venta>",views.seleccionarventa,name="seleccionarventa"),
    path("editarventa/",views.editarventa,name="editarventa"),
    path("borrarventa/<id_venta>",views.borrarventa,name="borrarventa"),
]