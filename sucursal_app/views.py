from django.shortcuts import render,redirect
from .models import sucursal

# Create your views here.

def inicio_vistasucursal(request):
    lossucursals = sucursal.objects.all()

    return render(request,"gestionarsucursal.html",{"missucursals":lossucursals})



def registrarsucursal(request):
    id_sucursal = request.POST["txtidsucursal"]
    direccion = request.POST["txtdireccion"]
    horario = request.POST["txthorario"]
    nombre= request.POST["txtnombre"]
    telefono = request.POST["txttelefono"]
    email = request.POST["txtemail"]
    codigo_postal = request.POST["txtcodigo_postal"]

    guardarsucursal = sucursal.objects.create(id_sucursal=id_sucursal, direccion=direccion, horario=horario, nombre=nombre,
                                            telefono=telefono,  email=email, codigo_postal=codigo_postal)

    return redirect("sucursal")

def seleccionarsucursal(request, id_sucursal):
    sucursale = sucursal.objects.get(id_sucursal = id_sucursal)

    return render(request,"editarsucursal.html",{"missucursals":sucursale})


def editarsucursal(request):
    id_sucursal = request.POST["txtidsucursal"]
    direccion = request.POST["txtdireccion"]
    horario = request.POST["txthorario"]
    nombre= request.POST["txtnombre"]
    telefono = request.POST["txttelefono"]
    email = request.POST["txtemail"]
    codigo_postal = request.POST["txtcodigo_postal"]
    

    sucursals = sucursal.objects.get(id_sucursal = id_sucursal)
    sucursals.direccion = direccion
    sucursals.horario = horario
    sucursals.nombre = nombre
    sucursals.telefono = telefono
    sucursals.email = email
    sucursals.codigo_postal = codigo_postal 
    

    sucursals.save()

    return redirect("sucursal")


def borrarsucursal(request, id_sucursal):
    sucu = sucursal.objects.get(id_sucursal = id_sucursal)
    sucu.delete()

    return redirect("sucursal")