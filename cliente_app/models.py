from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class cliente(models.Model):
    id_cliente = models.CharField(primary_key=True,max_length=6)
    nombre = models.CharField(max_length=45)
    apellido_materno = models.CharField(max_length=45)
    apellido_paterno = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre
    