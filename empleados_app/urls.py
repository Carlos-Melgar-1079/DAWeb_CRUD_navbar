from django.urls import path
from empleados_app import views 

urlpatterns = [
    path("empleados",views.inicio_vistaempleados,name="empleados"),
    path("registrarempleado/",views.registrarempleado,name="registrarempleado"),
    path("seleccionarempleado/<id_empleados>",views.seleccionarempleado,name="seleccionarempleado"),
    path("editarempleado/",views.editarempleado,name="editarempleado"),
    path("borrarempleado/<id_empleados>",views.borrarempleado,name="borrarempleado"),
]