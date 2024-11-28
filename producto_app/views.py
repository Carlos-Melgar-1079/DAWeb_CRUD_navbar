from django.shortcuts import render,redirect
from .models import producto

# Create your views here.

def inicio_vistaproductos(request):
    losproductos = producto.objects.all()

    return render(request,"gestionarproducto.html",{"misproducto":losproductos})



def registrarproducto(request):
    id_producto = request.POST["txtidproducto"]
    nombre = request.POST["txtnombre"]
    precio = request.POST["txtprecio"]
    tipo= request.POST["txttipo"]
    describcion = request.POST["txtdescribcion"]
    lote = request.POST["txtlote"]
    marca = request.POST["txtmarca"]

    guardarproveedor = producto.objects.create(id_producto=id_producto, nombre=nombre, precio=precio, tipo=tipo,
                                            describcion=describcion,  lote=lote, marca=marca)

    return redirect("productos")

def seleccionarproducto(request, id_producto):
    productor = producto.objects.get(id_producto = id_producto)

    return render(request,"editarproducto.html",{"misproductos":productor})


def editarproducto(request):
    id_producto = request.POST["txtidproducto"]
    nombre = request.POST["txtnombre"]
    precio = request.POST["txtprecio"]
    tipo= request.POST["txttipo"]
    describcion = request.POST["txtdescribcion"]
    lote = request.POST["txtlote"]
    marca = request.POST["txtmarca"]
    

    productos = producto.objects.get(id_producto = id_producto)
    productos.nombre = nombre
    productos.precio = precio
    productos.tipo = tipo
    productos.describcion = describcion
    productos.lote = lote
    productos.marca = marca 
    

    productos.save()

    return redirect("productos")


def borrarproducto(request, id_producto):
    product = producto.objects.get(id_producto = id_producto)
    product.delete()

    return redirect("productos")