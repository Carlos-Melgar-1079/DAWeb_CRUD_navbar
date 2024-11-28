from django.urls import path
from sucursal_app import views 

urlpatterns = [
    path("sucursal",views.inicio_vistasucursal,name="sucursal"),
    path("registrarsucursal/",views.registrarsucursal,name="registrarsucursal"),
    path("seleccionarsucursal/<id_sucursal>",views.seleccionarsucursal,name="seleccionarsucursal"),
    path("editarsucursal/",views.editarsucursal,name="editarsucursal"),
    path("borrarsucursal/<id_sucursal>",views.borrarsucursal,name="borrarsucursal"),
]