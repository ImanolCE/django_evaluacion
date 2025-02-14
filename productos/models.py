from django.db import models
from categorias.models import Categoria  #p para importar la tabla de categorías

# Create your models here.

# en este caso, el producto que se estaria utilizando de ejemplo, serina tenis.

from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)  # el nombre del tenis
    marca = models.CharField(max_length=50)  # la marca del tenis
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # el recio
    stock = models.IntegerField()  # la cantidad en el inventario
    descripcion = models.TextField(blank=True, null=True)  # descripción opcional
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # la fecha de registro
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1) # relaicon con la tabla de categoría

    def __str__(self):
        return f"{self.nombre} - {self.marca}"

