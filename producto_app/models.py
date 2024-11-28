from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class producto(models.Model):
    id_producto = models.CharField(primary_key=True,max_length=6)
    nombre = models.CharField(max_length=45)
    precio = models.CharField(max_length=45)
    tipo = models.CharField(max_length=45)
    describcion = models.CharField(max_length=45)
    lote = models.CharField(max_length=100)
    marca = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre
    