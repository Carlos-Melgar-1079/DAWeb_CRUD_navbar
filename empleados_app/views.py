from django.shortcuts import render,redirect
from .models import empleado

# Create your views here.

def inicio_vistaempleados(request):
    losempleador = empleado.objects.all()

    return render(request,"gestionarempleado.html",{"misempleadoo":losempleador})



def registrarempleado(request):
    id_empleados = request.POST["txtidempleados"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    telefono= request.POST["txttelefono"]
    horario = request.POST["txthorario"]
    email = request.POST["txtemail"]
    salario = request.POST["txtsalario"]

    guardarempleado = empleado.objects.create(id_empleados=id_empleados, nombre=nombre, apellido=apellido, telefono=telefono,
                                            horario=horario,  email=email, salario=salario)

    return redirect("empleados")

def seleccionarempleado(request, id_empleados):
    empleador = empleado.objects.get(id_empleados = id_empleados)

    return render(request,"editarempleado.html",{"misempleados":empleador})


def editarempleado(request):
    id_empleados = request.POST["txtidempleados"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    telefono= request.POST["txttelefono"]
    horario = request.POST["txthorario"]
    email = request.POST["txtemail"]
    salario = request.POST["txtsalario"]
    

    empleados = empleado.objects.get(id_empleados = id_empleados)
    empleados.nombre = nombre
    empleados.apellido = apellido
    empleados.telefono = telefono
    empleados.horario = horario
    empleados.email = email
    empleados.salario = salario
    

    empleados.save()

    return redirect("empleados")


def borrarempleado(request, id_empleados):
    product = empleado.objects.get(id_empleados = id_empleados)
    product.delete()

    return redirect("empleados")