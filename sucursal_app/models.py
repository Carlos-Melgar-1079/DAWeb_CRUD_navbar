from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class sucursal(models.Model):
    id_sucursal = models.CharField(primary_key=True,max_length=6)
    direccion = models.CharField(max_length=45)
    horario = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    codigo_postal= models.CharField(max_length=15)

    def __str__(self):
        return self.direccion
    