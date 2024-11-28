from django.urls import path
from producto_app import views 

urlpatterns = [
    path("productos",views.inicio_vistaproductos,name="productos"),
    path("registrarproducto/",views.registrarproducto,name="registrarproducto"),
    path("seleccionarproducto/<id_producto>",views.seleccionarproducto,name="seleccionarproducto"),
    path("editarproducto/",views.editarproducto,name="editarproducto"),
    path("borrarproducto/<id_producto>",views.borrarproducto,name="borrarproducto"),
]