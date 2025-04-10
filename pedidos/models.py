from django.db import models
from clientes.models import Cliente
from productos.models import Producto


# Create your models here.
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('completado', 'Completado'),
    ])

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nombre}"