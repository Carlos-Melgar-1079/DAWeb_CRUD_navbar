from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class empleado(models.Model):
    id_empleados = models.CharField(primary_key=True,max_length=6)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    horario = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    salario = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre
    