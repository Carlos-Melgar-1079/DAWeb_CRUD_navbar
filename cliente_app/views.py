from django.shortcuts import render,redirect
from .models import cliente

# Create your views here.

def inicio_vistaclientes(request):
    losclienter = cliente.objects.all()

    return render(request,"gestionarcliente.html",{"misclienter":losclienter})



def registrarcliente(request):
    id_cliente = request.POST["txtidcliente"]
    nombre = request.POST["txtnombre"]
    apellido_materno = request.POST["txtapellidomaterno"]
    apellido_paterno = request.POST["txtapellidopaterno"]
    email = request.POST["txtemail"]
    telefono = request.POST["txttelefono"]
    direccion = request.POST["txtdireccion"]

    guardarcliente = cliente.objects.create(id_cliente=id_cliente, nombre=nombre, apellido_materno=apellido_materno, apellido_paterno=apellido_paterno,
                                            email=email, telefono=telefono,  direccion=direccion)

    return redirect("clientes")

def seleccionarcliente(request, id_cliente):
    clientea = cliente.objects.get(id_cliente = id_cliente)

    return render(request,"editarcliente.html",{"misclienter":clientea})


def editarcliente(request):
    id_cliente = request.POST["txtidcliente"]
    nombre = request.POST["txtnombre"]
    apellido_materno = request.POST["txtapellidomaterno"]
    apellido_paterno = request.POST["txtapellidopaterno"]
    email = request.POST["txtemail"]
    telefono = request.POST["txttelefono"]
    direccion = request.POST["txtdireccion"]
    

    clientes = cliente.objects.get(id_cliente = id_cliente)
    clientes.nombre = nombre
    clientes.apellido_materno=apellido_materno
    clientes.email = email
    clientes.telefono = telefono
    clientes.apellido_paterno=apellido_paterno
    clientes.direccion = direccion
    

    clientes.save()

    return redirect("clientes")


def borrarcliente(request, id_cliente):
    usuario = cliente.objects.get(id_cliente = id_cliente)
    usuario.delete()

    return redirect("clientes")