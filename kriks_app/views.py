from django.shortcuts import render,redirect
from .models import Proveedores

# Create your views here.

def inicio_vistaproveedor(request):
    losproveedores = Proveedores.objects.all()

    return render(request,"gestionarProveedor.html",{"misproveedores":losproveedores})



def registrarProveedor(request):
    id_proveedor = request.POST["txtidproveedor"]
    nombre = request.POST["txtnombre"]
    horarios = request.POST["txthorarios"]
    email = request.POST["txtemail"]
    telefono = request.POST["txttelefono"]
    tipo = request.POST["txttipo"]
    direccion = request.POST["txtdireccion"]

    guardarproveedor = Proveedores.objects.create(id_proveedor=id_proveedor, nombre=nombre, horarios=horarios,
                                            email=email, telefono=telefono, tipo=tipo, direccion=direccion)

    return redirect("proveedor")

def seleccionarProveedor(request, id_proveedor):
    proveedores = Proveedores.objects.get(id_proveedor = id_proveedor)

    return render(request,"editarProveedor.html",{"misproveedores":proveedores})


def editarProveedor(request):
    id_proveedor = request.POST["txtidproveedor"]
    nombre = request.POST["txtnombre"]
    horarios = request.POST["txthorarios"]
    email = request.POST["txtemail"]
    telefono = request.POST["txttelefono"]
    tipo = request.POST["txttipo"]
    direccion = request.POST["txtdireccion"]
    

    proovedor = Proveedores.objects.get(id_proveedor = id_proveedor)
    proovedor.nombre_empresa = nombre
    proovedor.horarios = horarios
    proovedor.email = email
    proovedor.telefono = telefono
    proovedor.tipo = tipo
    proovedor.direccion = direccion
    

    proovedor.save()

    return redirect("proveedor")


def borrarProveedor(request, id_proveedor):
    trabajador = Proveedores.objects.get(id_proveedor = id_proveedor)
    trabajador.delete()

    return redirect("proveedor")