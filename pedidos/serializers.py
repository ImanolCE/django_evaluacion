from rest_framework import serializers
from clientes.models import Cliente
from productos.models import Producto
from .models import Pedido
from clientes.serializers import ClienteSerializer  # ¡Nuevo import!
from productos.serializers import ProductoSerializer  # ¡Nuevo import!

class PedidoSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)  # Solo lectura en GET
    producto = ProductoSerializer(read_only=True)
    cliente_id = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all(), source='cliente', write_only=True)  # Para POST/PUT
    producto_id = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all(), source='producto', write_only=True)

    class Meta:
        model = Pedido
        fields = ['id', 'cliente', 'producto', 'cliente_id', 'producto_id', 'cantidad', 'fecha', 'estado']

# def validate(self, data):
#     producto = data['producto']
#     if data['cantidad'] > producto.stock:
#         raise serializers.ValidationError("No hay suficiente stock.")
#     return data