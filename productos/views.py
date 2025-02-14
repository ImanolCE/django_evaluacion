from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer

from rest_framework.permissions import IsAuthenticated

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()  # Consulta todos los productos
    serializer_class = ProductoSerializer  # Usa el serializador creado
    permission_classes = [IsAuthenticated]  # para que solo usuarios autenticados pueden acceder

